import sqlite3
from fastapi import FastAPI
import uvicorn

app = FastAPI()

conn = sqlite3.connect("employees.db",check_same_thread=False)
cursor = conn.cursor()

def create_employees():
    cursor.execute("CREATE TABLE IF NOT EXISTS Employees (id int PRIMARY KEY, name varchar(50), dept varchar(30))")

def insert_employees():
    employees = [
        (1,"Daksh",'CSE'),
        (2,"Jay",'IT'),
        (3,"Chandana",'CSE'),
        (4,"Atoshi",'CSE'),
        (5,"Sri",'IT')
        ]
    cursor.executemany("INSERT OR IGNORE INTO Employees(id, name, dept) VALUES (?,?,?)", employees)
    conn.commit()

@app.get('/')
def get_data():
    return {"message": "The connection has been established successfully"} 

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
    cursor.execute("SELECT * FROM Employees WHERE id=?",(employee_id,))
    rows = cursor.fetchone()
    if rows is None:
        return {"error": "The employee ID does not exist"}
    
    return ({
            "id": rows[0],
            "name": rows[1],
            "department": rows[2]
    })

if __name__ == "__main__":
    create_employees()
    insert_employees()