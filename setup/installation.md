# Installation and Readiness Check

One consistent, zero-cost environment for everyone. Complete **every** step and the
[readiness check](#7-final-readiness-check) **before Day 1**. Supported systems: Windows 10/11 and macOS.

> Free tiers can change. The instructor re-checks the Render and Neon plans before delivery. This guide follows the
> *Participant Environment Guide v2 (Sep 30, 2026)*, which is still pending clean-computer validation.

## Approved stack

| Work | Tool | Used for |
|---|---|---|
| Code | **Python 3.13** + **VS Code** | write, run, debug, and test Django code |
| Web API | **Django 5.2 LTS** + **Django REST Framework 3.16** | models, serializers, endpoints, auth, tests |
| Local data | **SQLite** + **DB Browser for SQLite** | simple local database and visual inspection |
| API requests | **Postman Desktop** | send requests, tokens, and JSON bodies; save collections |
| Source | **Git** + **GitHub Free** | version history, submission, deployment source |
| Production | **Render Free** + **Neon PostgreSQL Free** | deploy the API with a persistent database |

Install in this order: **1** Python → **2** VS Code + extensions → **3** Git → **4** Postman + DB Browser →
**5** accounts → **6** this repository → **7** readiness check.

---

## 1. Python 3.13

<details open><summary><b>Windows</b></summary>

1. Download the latest **Python 3.13.x Windows installer (64-bit)** from https://www.python.org/downloads/.
2. Run it. Tick **Add python.exe to PATH**. Keep **pip** and **venv** selected.
3. Close all terminals, open a **new** PowerShell, and verify:

```powershell
py --version            # Python 3.13.x
py -m pip --version     # pip ... from C:\...
```

`py` not recognised? Restart Windows. Still failing → re-run the installer with the PATH/launcher options.
Never download Python from an unofficial site.
</details>

<details><summary><b>macOS</b></summary>

1. Download the latest **Python 3.13.x macOS 64-bit universal2 installer** from https://www.python.org/downloads/
   and run the `.pkg`. (Do not use the system Python that ships with macOS.)
2. Open **Terminal** (Applications → Utilities) and verify:

```bash
python3 --version          # Python 3.13.x
python3 -m pip --version
```
</details>

## 2. VS Code and extensions

1. Install VS Code from https://code.visualstudio.com/download. Windows: enable **Add to PATH**. macOS: drag it
   to Applications, then run **Shell Command: Install 'code' command in PATH** from the Command Palette
   (Cmd+Shift+P).
2. Extensions (all by **Microsoft**): **Python**, **Pylance**, **Python Debugger**.
3. Open **Terminal → New Terminal** and run `py --version` (Windows) / `python3 --version` (macOS).

**Pass:** VS Code opens, the 3 extensions show *Installed*, and the integrated terminal reports Python 3.13.

## 3. Git

- **Windows:** install the 64-bit **Git for Windows** from https://git-scm.com/install/ with the default options
  (keep the credential manager).
- **macOS:** run `git --version`. If macOS offers the *Command Line Developer Tools*, accept.

Then, in a new terminal:

```bash
git --version
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"     # the email of your GitHub account
git config --global init.defaultBranch main
git config --global --list
```

## 4. Postman and DB Browser for SQLite

**Postman Desktop:** install it from the official site (on a Mac choose Apple Silicon or Intel) and send this
request:

| Method | URL | Expected |
|---|---|---|
| GET | `https://postman-echo.com/get` | `200 OK` |

**DB Browser for SQLite:** install the standard installer from https://sqlitebrowser.org/dl/. Open it once and check
that *Open Database*, *Database Structure* and *Browse Data* are visible. Do not create a database: Django creates
`db.sqlite3` for you. (macOS Gatekeeper warning: confirm the download came from sqlitebrowser.org and allow it in
*Privacy & Security*.)

## 5. Free accounts

| Service | Purpose | Notes |
|---|---|---|
| GitHub | repositories, submission, Render connection | verify your email, **enable two-factor authentication**, sign in to GitHub from VS Code (Accounts icon) |
| Postman | save the Task API collection | free individual plan |
| Neon | hosted PostgreSQL | create the account and open the dashboard. **Do not create or share credentials yet.** |
| Render | hosts the API | create the account, **connect your GitHub account**, and check that *New → Web Service* can see your repositories |

> **Never commit or share credentials.** Database URLs, secret keys, tokens, and passwords never belong in Git,
> screenshots, public Postman workspaces, or chat messages.

## 6. This repository and the shared virtual environment

All five **exercises** run from one virtual environment at the root of this repository. (Your **project** gets its
own environment on Day 1.)

```powershell
# Windows PowerShell
git clone <bootcamp-repository-url>
cd django-rest-api-bootcamp
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m django --version          # 5.2.x
```

```bash
# macOS
git clone <bootcamp-repository-url>
cd django-rest-api-bootcamp
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m django --version          # 5.2.x
```

**PowerShell blocks `Activate.ps1`?** Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirm, close
PowerShell, open it again, and activate again.

**VS Code interpreter:** Ctrl+Shift+P / Cmd+Shift+P → **Python: Select Interpreter** → choose the one inside
`.venv`. New terminals must show `(.venv)` at the start of the prompt.

## 7. Final readiness check

Run the Day 1 exercise's first command, then start a throw-away Django check:

```bash
cd days/day-01/exercise
python manage.py check              # System check identified no issues (0 silenced).
cd ../../..

python -c "import json; print(json.dumps({'title': 'Environment check', 'completed': False}))"
```

| Check | Windows | macOS | Pass result |
|---|---|---|---|
| Python | `py --version` | `python3 --version` | Python 3.13.x |
| pip | `py -m pip --version` | `python3 -m pip --version` | shows an installed path |
| VS Code | `code --version` | `code --version` | prints a version |
| Git | `git --version` | `git --version` | prints a version |
| Virtual env | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` | prompt starts with `(.venv)` |
| Django | `python -m django --version` | same | 5.2.x |
| Django project | `python manage.py check` (Day 1 exercise) | same | no issues |
| Postman | Postman Echo GET | same | 200 OK |
| SQLite | open DB Browser | same | app opens |
| Accounts | GitHub + Neon + Render | same | dashboards open |

### Submit before Day 1 (at least 48 hours before)

- Screenshot or text output of the Python, Git, and Django versions
- Screenshot of the installed VS Code extensions
- The Postman Echo response showing `200 OK`
- Your GitHub username and confirmation that the GitHub, Neon, and Render dashboards open
- Any unresolved error copied as **text** (not only a screenshot)

If any check fails, use [`troubleshooting.md`](troubleshooting.md) and attend the **setup clinic** before Day 1.
