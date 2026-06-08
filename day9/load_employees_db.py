import csv
import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()


def validate_record(row):
    db_employee_id = cursor.execute("SELECT employee_id from Employees WHERE employee_id=?", (row[0],) )
    if len(row) != 3 or "" in row:
        return False
    if cursor.fetchone():
        return False
    return True


def save_to_database(row):
    cursor.execute(
        """
        INSERT OR IGNORE INTO Employees
        (employee_id, name, department)
        VALUES (?, ?, ?)
        """,
        row
    )


def generate_report(total_records, success_records, invalid_records, report):
    print("\nImport Report")
    print("-" * 30)
    print(f"Total Records: {total_records}")
    print(f"Success: {success_records}")
    print(f"Failed: {invalid_records}")

    if report:
        print("\nFailed Records:")
        for rep in report:
            print(rep)


if __name__ == "__main__":

    report = []
    total_records = 0
    success_records = 0
    invalid_records = 0

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            employee_id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(50)
        )
    """)

    with open('employees_import_test.csv', newline='') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip header row
        next(csvReader)

        for row in csvReader:
            total_records += 1
            

            if validate_record(row):
                save_to_database(row)
                success_records += 1
            else:
                invalid_records += 1
                report.append(f"Invalid record: {row}")

    conn.commit()

    generate_report(
        total_records,
        success_records,
        invalid_records,
        report
    )

    conn.close()