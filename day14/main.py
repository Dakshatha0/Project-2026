from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, status
import sqlite3

app = FastAPI()
conn = sqlite3.connect(
    "employees.db",
    check_same_thread=False
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Employees (employee_id INT PRIMARY KEY, name TEXT, department TEXT, status TEXT)")

class Employee(BaseModel):
    employee_id: int
    name: str = Field(min_length = 1)
    department: str = Field(min_length = 1)
    status: str = 'Active'

class EmployeeUpdate(BaseModel):
    name: str = Field(min_length = 1)
    department: str = Field(min_length = 1)
    status: str = 'Active'

@app.get('/')
def get_data():
    return {
        "message": "Connection established successfully"
    }

@app.post('/employees')
def post_employee(employee: Employee):
    cursor.execute("""INSERT OR IGNORE INTO Employees (employee_id, name, department, status) VALUES (?,?,?,?)""", (employee.employee_id,
                                                                                                      employee.name,
                                                                                                      employee.department,
                                                                                                      employee.status))
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
            "department": row[2],
            "status": row[3]
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
            "department": rows[2],
            "status": rows[3]
    })

@app.put('/employees/{employee_id}')
def employee_update(employee_id: int, employee: EmployeeUpdate):
    cursor.execute("UPDATE Employees SET name=?, department=? WHERE employee_id=?", (employee.name, employee.department, employee_id))
    conn.commit()
    if cursor.rowcount==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return {"message": status.HTTP_200_OK}

@app.delete('/employees/{employee_id}')
def employee_delete(employee_id: int):
    cursor.execute("UPDATE Employees SET status='Inactive' WHERE employee_id=?", (employee_id,))
    conn.commit()
    if cursor.rowcount==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return {"message": status.HTTP_200_OK}