import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

def create_database_emp():
    cursor.execute(
    "CREATE TABLE IF NOT EXISTS Employees(id int PRIMARY KEY, name varchar(50), department varchar(50), salary int, experience_years int, FOREIGN KEY (department) REFERENCES Department(dept_id));"
    )
    print("Database Employees Created")

def insert_employees():
    employees = [
        ("10","Daksh",1,"18000000", "10"),
        ("20","Jay",2,"20000000", "12"),
        ("30","Chandana",1,"21000000", "14"),
        ("40","Atoshi",1,"22000000", "15"),
        ("50","Sri",3,"23000000", "20")
        ]
    cursor.executemany(
        "INSERT OR IGNORE INTO Employees(id, name, department, salary, experience_years) VALUES (?,?,?,?,?)", employees
    )
    conn.commit()
    print("Database Employees have been inserted with employees")

def create_database_dept():
    print("Created DEPT Database: ")
    cursor.execute("CREATE TABLE IF NOT EXISTS Department(dept_id INT PRIMARY KEY, dept_name varchar(100));")

def insert_dept():
    departments = [(1, "CSE-B"), (2, "IT")]
    cursor.executemany("INSERT OR IGNORE INTO Department(dept_id, dept_name) VALUES (?,?)", departments)
    conn.commit()

def show_employee_departments():
    print("\n")
    print("Employees with departments: ")
    cursor.execute("SELECT e.id, e.name, d.dept_id, d.dept_name FROM Employees e INNER JOIN Department d ON e.department = d.dept_id")
    for row in cursor.fetchall():
        print(row)
    
def show_cse_employees():
    print("\n")
    print("Employees with Dept = CSE-B: ")
    cursor.execute("SELECT e.id, e.name, d.dept_name FROM Employees e INNER JOIN Department d ON e.department = d.dept_id WHERE d.dept_id=1;")
    for row in cursor.fetchall():
        print(row)

def emp_in_each_dept():
    print("\n")
    print("Employee count in each department: ")
    cursor.execute("SELECT d.dept_name, COUNT(*) from Employees e INNER JOIN Department d ON e.department = d.dept_id GROUP BY d.dept_id;")
    for row in cursor.fetchall():
        print(row)
def show_all_employees():
    print("\n")
    print("Employees present in the database:")
    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        print(row)

def show_engineering_employees():
    print("\n")
    print("Employees in CSE-B Dept: ")
    cursor.execute("SELECT * from Employees WHERE department=1;")
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
    create_database_emp()
    create_database_dept()
    insert_employees()
    insert_dept()
    show_employee_departments()
    show_cse_employees()
    emp_in_each_dept()
    show_all_employees()
    show_engineering_employees()
    show_highest_paid_employee()
    show_top_paid_employees()
    show_employee_count()

    conn.close()
    