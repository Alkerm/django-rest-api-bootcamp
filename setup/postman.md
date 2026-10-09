# Postman for the Task API

Postman is for **exploring and demonstrating** the API. It does not replace the automated tests you write on Day 4.

## Import the ready-made collection (recommended)

1. Postman → **Import** → choose [`assets/postman/task-management-api.postman_collection.json`](../assets/postman/task-management-api.postman_collection.json).
2. Postman → **Import** → choose [`assets/postman/local-django.postman_environment.json`](../assets/postman/local-django.postman_environment.json).
   It creates the `Local Django` environment with every variable the collection uses:

   | Variable | Initial value |
   |---|---|
   | `base_url` | `http://127.0.0.1:8000` |
   | `username` / `other_username` | `alice` / `bob` (change them to your two test users) |
   | `password` / `other_password` | *(empty)*: type each password in **Current value** only |
   | `token` / `other_token` / `task_id` | *(empty)*: filled in automatically by the requests |

3. Select the `Local Django` environment (top right) before sending requests.
4. Send **Get token** first. Its post-response script stores the token in `{{token}}` automatically.

For production, duplicate the environment as `Render` and set `base_url` to `https://<your-app>.onrender.com`.

## Requests in the collection

| Request | Method + URL | Body / auth | Expected |
|---|---|---|---|
| Get token | `POST {{base_url}}/api/auth/token/` | JSON `{"username": "{{username}}", "password": "{{password}}"}` | `200` + token |
| List tasks | `GET {{base_url}}/api/tasks/` | `Authorization: Token {{token}}` | `200` + array |
| Create task | `POST {{base_url}}/api/tasks/` | token + JSON task fields | `201` + task |
| Retrieve task | `GET {{base_url}}/api/tasks/{{task_id}}/` | token | `200` |
| Replace task | `PUT {{base_url}}/api/tasks/{{task_id}}/` | token + all writable fields | `200` |
| Update task | `PATCH {{base_url}}/api/tasks/{{task_id}}/` | token + changed fields | `200` + task |
| Validation error | `POST {{base_url}}/api/tasks/` | token + JSON `{"title": "   ", "status": "FINISHED", "due_date": "2020-01-01"}` | `400` with errors on `title`, `status` and `due_date` |
| Get token (other user) | `POST {{base_url}}/api/auth/token/` | JSON with `{{other_username}}` / `{{other_password}}` | `200`, stored in `{{other_token}}` |
| Other user retrieves my task | `GET {{base_url}}/api/tasks/{{task_id}}/` | `Authorization: Token {{other_token}}` | `404` |
| Other user updates my task | `PATCH {{base_url}}/api/tasks/{{task_id}}/` | other token + `{"title": ...}` | `404`, title unchanged |
| Other user deletes my task | `DELETE {{base_url}}/api/tasks/{{task_id}}/` | other token | `404`, task still exists |
| Delete task | `DELETE {{base_url}}/api/tasks/{{task_id}}/` | token | `204` |
| No token | `GET {{base_url}}/api/tasks/` | none | `401` |

**Create task** stores the new id in `{{task_id}}`, so the following requests use it. Run the requests **in order**
(or with the Collection Runner): the four *other user* requests are the Day 3 two-user check and part of the Day 5 demo.

## Saving the token yourself

In a request's **Scripts → Post-response** tab:

```javascript
const body = pm.response.json();
pm.environment.set("token", body.token);
```

The label may differ slightly between Postman versions.

## Security rules

- Never export, share, or screenshot an environment that contains a real token, password, database URL, or secret key.
- Keep real values in **Current value** (local only), not in *Initial value* (which is synced and shared).
- The collection in this repository contains placeholders only.
