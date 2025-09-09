# TaskFlow — Flask + React + Postgres (CRUD)

A small, interview-ready full-stack CRUD app for **Tasks**.

- **Backend:** Flask + SQLAlchemy + Flask-Migrate (Alembic) + PostgreSQL  
- **Frontend:** React (Create React App) — single page at `frontend/src/App.js`  
- **Auth:** None (kept simple for interviews)  
- **UI Footer:** “Created by Sunil @ 2025”


## ✅ Quick Start (GitHub → Local run)

### 0) Clone the repo from GitHub
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


## 🧭 What’s inside

.
├─ backend/
│ ├─ app.py # Flask app init
│ ├─ routes.py # /tasks CRUD endpoints
│ ├─ models.py # SQLAlchemy model: Tasks
│ ├─ config.py # env-based settings
│ ├─ migrations/ # Alembic (Flask-Migrate)
│ ├─ requirements.txt # backend dependencies
│ ├─ wsgi.py # Gunicorn entry (for deploy)
│ └─ Procfile # (optional for some hosts)
└─ frontend/
├─ src/App.js # React UI (CRUD)
├─ package.json
└─ .env # REACT_APP_API_URL




1) Backend (Flask)

Prereqs: Python 3.10+, PostgreSQL running locally

cd backend
python -m venv .venv
# Windows (PowerShell):
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt


Set environment variables (adjust DB URL if needed):

# Windows (PowerShell)
$env:FLASK_APP = "app.py"
$env:DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/crud_db"

# macOS/Linux
export FLASK_APP="app.py"
export DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost:5432/crud_db"


Run migrations & start server:

flask db upgrade
flask run --host=127.0.0.1 --port=5000


Backend is now at http://127.0.0.1:5000




2) Frontend (React)

Open a new terminal window:

cd frontend
npm install
# point UI to the backend API:
echo REACT_APP_API_URL=http://127.0.0.1:5000 > .env
npm start


Open http://localhost:3000




API Overview (no auth)

GET /tasks — list tasks
Optional filter: ?completed=true or ?completed=false

GET /tasks/<id> — get one

POST /tasks — create

{ "title": "Buy milk" }


PUT /tasks/<id> — full update

{ "title": "Buy milk and eggs", "completed": true }


PATCH /tasks/<id> — partial update

{ "completed": true }


DELETE /tasks/<id> — delete

List response example

{
  "message": "ok",
  "data": [
    { "id": 1, "title": "Buy milk", "completed": false, "created_at": "2025-09-09T08:00:00" }
  ]
}


Quick cURL tests

# create a task
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"First task\"}"

# list tasks
curl http://127.0.0.1:5000/tasks

# toggle complete
curl -X PATCH http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{\"completed\": true}"

# delete
curl -X DELETE http://127.0.0.1:5000/tasks/1
