import json
def view_employees(data):
            emp_id = int(input("Enter Employee ID: "))
            view_data = {}
            for d in data:
                if d['id'] == emp_id:
                    view_data = d
                    break
            if view_data:
                return view_data
            else:
                print("The employee ID data does not exist")

def display_employees(data):
            return data

def add_employees(data):
        try:
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            ID_exists = False
            for d in data:
                 if d['id'] == emp_id:
                      ID_exists = True
            if ID_exists == False:
                data.append({
                    "id": emp_id,
                    "name": name,
                    "department": dept
                })
                with open("employees.json", "w") as jsonfile:
                    json.dump(data, jsonfile, indent=4)
            else:
                 print("Employee ID already exists")
        except ValueError:
            print("Enter appropriate Employee ID/Name/Dept. Note: Employee ID should be a number")
        return data

if __name__ == "__main__":
            try:
                with open("employees.json", "r") as jsonfile:
                    data = json.load(jsonfile)
            except FileNotFoundError:
                print("Employees.json file not found. Please check the file location")
            
            while True:
                print("1. View All Employees")
                print("2. View Employee")
                print("3. Add Employee")
                print("4. Exit")

                num = int(input("Choose option: "))

                match num:
                    case 1:
                        print(display_employees(data))
                    case 2:
                        print(view_employees(data))
                    case 3:
                        print(add_employees(data))
                    case 4:
                        break
                    case _:
                          print("Enter a valid number from above")
