"""
Day 4 worked example - API tests for the personal Notes API (see day-03/example).

Structure of every test:   ARRANGE (data)  ->  ACT (one request)  ->  ASSERT (status, body, database)
"""
from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Note


class NoteAPITests(APITestCase):
    # setUp runs before EACH test, in a fresh empty test database -> tests never depend on each other.
    def setUp(self):
        self.sara = User.objects.create_user(username="sara", password="sara-test-pass")
        self.omar = User.objects.create_user(username="omar", password="omar-test-pass")
        self.sara_token = Token.objects.create(user=self.sara)
        self.omar_token = Token.objects.create(user=self.omar)
        self.sara_note = Note.objects.create(author=self.sara, text="Buy milk")
        self.list_url = reverse("note-list")                                  # /api/notes/
        self.sara_note_url = reverse("note-detail", args=[self.sara_note.id])  # /api/notes/<id>/

    def login_as(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    # --- a SUCCESS test: allowed work succeeds and changes the database
    def test_create_note_sets_author(self):
        self.login_as(self.omar_token)                                          # ARRANGE

        response = self.client.post(self.list_url, {"text": "Call mom"}, format="json")  # ACT

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)          # ASSERT response
        self.assertEqual(response.data["author"], "omar")
        note = Note.objects.get(id=response.data["id"])                          # ASSERT database
        self.assertEqual(note.author, self.omar)

    # --- a FAILURE test: forbidden work fails AND changes nothing
    def test_other_user_cannot_edit_note(self):
        self.login_as(self.omar_token)

        response = self.client.patch(self.sara_note_url, {"text": "Hacked"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.sara_note.refresh_from_db()           # re-read the row - the Python object is not updated automatically
        self.assertEqual(self.sara_note.text, "Buy milk")

    # --- a VALIDATION test
    def test_past_reminder_is_rejected(self):
        self.login_as(self.sara_token)
        yesterday = timezone.localdate() - timedelta(days=1)

        response = self.client.post(
            self.list_url, {"text": "Old reminder", "remind_on": yesterday.isoformat()}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("remind_on", response.data)              # the error is reported under the field name
        self.assertEqual(Note.objects.count(), 1)              # nothing was saved

    # --- an AUTHENTICATION test
    def test_anonymous_request_is_rejected(self):
        response = self.client.get(self.list_url)               # no credentials() call -> anonymous

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# Useful assertions:
#   assertEqual(a, b)   assertNotEqual   assertTrue(x)   assertFalse(x)   assertIn(item, container)   assertNotIn
# Useful client calls:
#   self.client.get(url)   .post(url, data, format="json")   .put(...)   .patch(...)   .delete(url)
#   self.client.credentials()      <- with no arguments: remove the token again
# Run one test only:
#   python manage.py test notes.tests.NoteAPITests.test_create_note_sets_author
