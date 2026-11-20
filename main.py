import os
from fastapi import FastAPI
from fastapi.responses import FileResponse

from controllers import StudentController
from repositories import PostgresStudentRepo
from services import NaiveStudentService

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not configured")

repo = PostgresStudentRepo(DATABASE_URL)
service = NaiveStudentService(repo)
controller = StudentController(service)

app.include_router(controller.router)


@app.get("/")
def home():
    return FileResponse("index.html")
