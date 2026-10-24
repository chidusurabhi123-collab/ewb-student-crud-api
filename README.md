Students Database CRUD API - EWB Internship Project

Project Type: Individual backend development project
Objective: Build a Python backend to manage student records with Create, Read, Update, Delete operations using FastAPI + SQLite.
A clean, production-ready REST API that lets you add, list, view, update, and delete student records. Data is persisted in SQLite (students.db). Includes Swagger docs, validation, and proper error handling as per EWB review checklist.
FastAPI
Python
SQLite
________________________________________
✨ Features
•	CRUD: Full Create / Read / Update / Delete
•	Persistent Storage: SQLite with SQLAlchemy ORM
•	Validation: Pydantic schemas, 404 handling for missing records
•	Docs: Auto-generated Swagger UI at /docs and ReDoc at /redoc
•	Clean Code: Separated models.py, schemas.py, database.py, main.py
🛠 Tech Stack
•	Python 3.10+
•	FastAPI
•	SQLAlchemy
•	SQLite
•	Uvicorn (ASGI server)
•	Pydantic v2
📁 Project Structure
ewb-project/├── main.py          # FastAPI app & routes├── models.py        # SQLAlchemy Student model├── schemas.py       # Pydantic request/response schemas├── database.py      # SQLite engine & session├── requirements.txt # Dependencies├── students.db      # Auto-created SQLite DB (gitignored)├── .gitignore└── README.md
📋 Prerequisites
•	Python 3.10+ installed (you have 3.14)
•	VS Code
•	Git
🚀 How to Run - Step by Step (Windows PowerShell)
1. Clone & open in VS Code
git clone https://github.com/YOUR_USERNAME/ewb-student-crud-api.gitcd ewb-projectcode .
2. Create virtual environment & activate
python -m venv .venv.\.venv\Scripts\Activate.ps1# If error: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
3. Install dependencies
pip install -r requirements.txt# If requirements.txt missing:pip install fastapi uvicorn sqlalchemy pydantic
4. Run the server
python -m uvicorn main:app --reload
You should see:
INFO: Uvicorn running on http://127.0.0.1:8000
5. Open docs
•	Swagger UI: http://127.0.0.1:8000/docs <- Test here
•	ReDoc: http://127.0.0.1:8000/redoc
•	OpenAPI JSON: http://127.0.0.1:8000/openapi.json
🔌 API Endpoints
Method	Endpoint	Purpose	Status Code
POST	/students	Create a new student	200 OK
GET	/students	List all students (with pagination)	200 OK
GET	/students/{student_id}	Get one student by unique ID	200 / 404
PUT	/students/{student_id}	Update student details	200 / 404
DELETE	/students/{student_id}	Delete student	200 / 404
Student Fields
•	student_id (str, unique, required) e.g., "STU001"
•	name (str, required)
•	dob (date, optional) YYYY-MM-DD
•	email (str, optional)
•	phone (str, optional)
•	course (str, optional)
•	address (str, optional)
🧪 How to Test - Examples
1. Create a Student
Swagger: POST /students > Try it out > Paste JSON > Execute
{  "student_id": "STU001",  "name": "Chidambar Bharadwaj",  "dob": "2006-05-10",  "email": "chidambar@example.com",  "phone": "9876543210",  "course": "BCA",  "address": "Chikodi, Karnataka"}
cURL:
curl -X POST http://127.0.0.1:8000/students ^-H "Content-Type: application/json" ^-d "{\"student_id\":\"STU001\", \"name\":\"Chidambar Bharadwaj\", \"email\":\"chidambar@example.com\", \"course\":\"BCA\"}"
Response:
{  "student_id": "STU001",  "name": "Chidambar Bharadwaj",  "dob": "2006-05-10",  "email": "chidambar@example.com",  "phone": "9876543210",  "course": "BCA",  "address": "Chikodi, Karnataka",  "id": 1}
2. List All Students
GET http://127.0.0.1:8000/students
Response is array of students.
3. Get One Student
GET http://127.0.0.1:8000/students/STU001
4. Update Student
PUT http://127.0.0.1:8000/students/STU001
{  "course": "BCA 2nd Year",  "phone": "9999999999"}
5. Delete Student
DELETE http://127.0.0.1:8000/students/STU001
Response:
{"detail": "Deleted"}
🗃️ Database
•	SQLite file students.db auto-created on first run
•	Located at project root
•	To reset: delete students.db and restart server
✅ Review Checklist Covered
•	All 4 CRUD operations work
•	SQLite persists data
•	Input validation (required fields, unique student_id)
•	404 handling for missing records
•	Organized code (models/schemas/database separated)
•	README with reproducible steps
•	requirements.txt included
•	No secrets or real personal data committed
