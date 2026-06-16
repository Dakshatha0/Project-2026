from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, status
import sqlite3

app = FastAPI()
conn = sqlite3.connect(
    "employees.db",
    check_same_thread=False
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Employees (employee_id INT PRIMARY KEY, name TEXT, department TEXT)")

class Employee(BaseModel):
    employee_id: int
    name: str = Field(min_length = 1)
    department: str = Field(min_length = 1)

@app.post('/employees')
def post_employee(employee: Employee):
    
    cursor.execute("""INSERT OR IGNORE INTO Employees (employee_id, name, department) VALUES (?,?,?)""", (employee.employee_id,
                                                                                                      employee.name,
                                                                                                      employee.department))
    conn.commit()
    return {
        "message": "Employee Created",
        "employee": employee
    }

@app.get('/employees')
def get_employees():
    employees = []
    cursor.execute("SELECT * FROM Employees")
    rows = cursor.fetchall()
    for row in rows:
        employees.append({
            "id": row[0],
            "name": row[1],
            "department": row[2]
        })
    return employees

@app.get('/employees/{employee_id}')
def get_employee_data(employee_id: int):
    cursor.execute(
    "SELECT * FROM Employees WHERE employee_id=?",
    (employee_id,)
    )
    rows = cursor.fetchone()
    if rows is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return ({
            "id": rows[0],
            "name": rows[1],
            "department": rows[2]
    })