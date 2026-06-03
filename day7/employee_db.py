import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

def create_database():
    cursor.execute(
    "CREATE TABLE IF NOT EXISTS Employees(id int PRIMARY KEY, name varchar(50), department varchar(50), salary int, experience_years int);"
    )
    print("Database Employees Created")

def insert_employees():
    employees = [
        ("10","Daksh","CSE-B","18000000", "10"),
        ("20","Jay","CSE","20000000", "12"),
        ("30","Chandana","CSE-B","21000000", "14"),
        ("40","Atoshi","CSE-B","22000000", "15"),
        ("50","Sri","CSE-B","23000000", "20")
        ]
    cursor.executemany(
        "INSERT OR IGNORE INTO Employees(id, name, department, salary, experience_years) VALUES (?,?,?,?,?)", employees
    )
    conn.commit()
    print("Database Employees have been inserted with employees")

def show_all_employees():
    print("\n")
    print("Employees present in the database:")
    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        print(row)

def show_engineering_employees():
    print("\n")
    print("Employees in CSE-B Dept: ")
    cursor.execute("SELECT * from Employees WHERE department='CSE-B';")
    for row in cursor.fetchall():
        print(row)

def show_highest_paid_employee():
    print("\n")
    print("Employee with highest paid salary: ")
    cursor.execute("SELECT * from Employees ORDER BY salary DESC LIMIT 1")
    print(cursor.fetchone())

def show_top_paid_employees():
    print("\n")
    print("Top three employees with highest paid salary: ")
    cursor.execute("SELECT * from Employees ORDER BY salary DESC LIMIT 3")
    for row in cursor.fetchall():
        print(row)

def show_employee_count():
    print("\n")
    print("Total count of employees: ")
    cursor.execute("SELECT COUNT(*) FROM Employees")
    print(cursor.fetchone())

if __name__ == "__main__":
    create_database()
    insert_employees()
    show_all_employees()
    show_engineering_employees()
    show_highest_paid_employee()
    show_top_paid_employees()
    show_employee_count()

    conn.close()
    