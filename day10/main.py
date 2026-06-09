#To run: uvicorn main:app --reload main is the name of the py file, app is the FastAPI object created

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/employees")
def get_employees():
    return [
        {"id": 101, "employee": "Daksh"},
        {"id": 102, "employee": "Jay"}
    ]

@app.get("/employees/{employee_id}")
def get_employee_id(employee_id: int):
    return {"employee_id": employee_id}