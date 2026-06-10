from fastapi import FastAPI

app = FastAPI()

employees = [
    {
        "id": 101,
        "name": "Daksh",
        "department": "Engineering"
    },
    {
        "id": 102,
        "name": "Jay",
        "department": "HR"
    },
    {
        "id": 103,
        "name": "Chandana",
        "department": "Engineering"
    }
]

@app.get("/")
def home():
    return {"message": "Employee API"}

@app.get('/employees')
def get_employees():
    return employees

@app.get("/employees/search")
def get_emp_by_dept(department: str):
    result = []
    for employee in employees:
        if employee["department"] == department:
            result.append(employee)
    return result

@app.get('/employees/{id}')
def get_employee_id(id: int):
    for employee in employees:
        if employee["id"] == id:
            return employee
    return {"error": "Employee ID does not exist"}