# Day 2 · Task 5B: CRUD checklist

Send each request with the **browsable API** (http://127.0.0.1:8000/api/books/) or **Postman**, in this order.
Fill in the **Actual status** column, then check the database (admin or DB Browser) after each write.

> Start from fresh sample data so the ids match:
> `python manage.py flush --no-input` then `python manage.py loaddata sample_data`

| # | Operation | Method + URL | Body (JSON) | Expected status | Expected database change | Actual status |
|---|---|---|---|---|---|---|
| 1 | List | `GET /api/books/` | none | `200` | none: 6 books returned, A-Z after Task 5A | |
| 2 | Create | `POST /api/books/create/` | `{"title": "Domain-Driven Design", "isbn": "9780000000073", "published_year": 2003, "available_copies": 2, "author": 2}` | `201` | new row id **7** in `catalog_book` | |
| 3 | Retrieve | `GET /api/books/7/` | none | `200` | none | |
| 4 | Full update | `PUT /api/books/7/update/` | `{"title": "Domain-Driven Design (Reference)", "isbn": "9780000000073", "published_year": 2015, "available_copies": 1, "author": 2}` | `200` | row 7: title, year and copies changed | |
| 5 | Partial update | `PATCH /api/books/7/update/` | `{"available_copies": 10}` | `200` | row 7: only `available_copies` changed | |
| 6 | Delete | `DELETE /api/books/7/delete/` | none | `204` | row 7 removed (6 books again) | |
| 7 | Missing id | `GET /api/books/7/` | none | `404` | none | |
| 8 | Invalid create | `POST /api/books/create/` | `{"title": "", "published_year": 2020}` | `400` | none: nothing saved | |
| 9 | Wrong method | `POST /api/books/` | `{}` | `405` | none | |

## Questions to answer (write 1-2 lines each)

1. In request #8, which fields returned errors, and which line of `create_book` produced them?
2. Why does request #9 return `405` and not `404`?
3. In request #2 you sent `"author": 2`, but the response also contains `"author_name"`. Where does that value come from?
