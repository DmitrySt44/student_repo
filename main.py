import os
from fastapi import FastAPI
from fastapi.responses import FileResponse

from controllers import StudentController
from repositories import PostgresStudentRepo
from services import NaiveStudentService

app = FastAPI()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:secretpassword@localhost:5432/students_db"
)

repo = PostgresStudentRepo(DATABASE_URL)
service = NaiveStudentService(repo)
controller = StudentController(service)

app.include_router(controller.router)


@app.get("/")
def home():
    return FileResponse("index.html")
