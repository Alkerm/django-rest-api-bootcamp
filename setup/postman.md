# Postman for the Task API

Postman is for **exploring and demonstrating** the API. It does not replace the automated tests you write on Day 4.

## Import the ready-made collection (recommended)

1. Postman → **Import** → choose [`assets/postman/task-management-api.postman_collection.json`](../assets/postman/task-management-api.postman_collection.json).
2. Postman → **Environments** → **+** → name it `Local Django`, then add:

   | Variable | Initial value |
   |---|---|
   | `base_url` | `http://127.0.0.1:8000` |
   | `username` | your test user, e.g. `alice` |
   | `password` | that user's local password (type it in **Current value** only) |
   | `token` | *(empty)* |

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
| Delete task | `DELETE {{base_url}}/api/tasks/{{task_id}}/` | token | `204` |
| No token | `GET {{base_url}}/api/tasks/` | none | `401` |

**Create task** stores the new id in `{{task_id}}`, so the following requests use it.

## Saving the token yourself

In a request's **Scripts → Post-response** tab:

```javascript
const data = pm.response.json();
pm.environment.set("token", data.token);
```

The label may differ slightly between Postman versions.

## Security rules

- Never export, share, or screenshot an environment that contains a real token, password, database URL, or secret key.
- Keep real values in **Current value** (local only), not in *Initial value* (which is synced and shared).
- The collection in this repository contains placeholders only.
