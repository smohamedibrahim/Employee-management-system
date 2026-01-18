# Employee Management Application
# Created by: Mohamed Ibrahim
# Purpose: Python practice project for fresher interviews

employee_list = []

def add_emp():
    emp_code = input("Enter Employee Code: ")
    emp_name = input("Enter Employee Name: ")
    emp_team = input("Enter Team/Department: ")
    emp_pay = input("Enter Monthly Salary: ")

    emp_data = {
        "code": emp_code,
        "name": emp_name,
        "team": emp_team,
        "salary": emp_pay
    }

    employee_list.append(emp_data)
    print("✔ Employee details saved successfully\n")

def show_all_emp():
    if len(employee_list) == 0:
        print("No employee data available\n")
        return

    print("---- Employee Records ----")
    for emp in employee_list:
        print(f"Code: {emp['code']} | Name: {emp['name']} | Team: {emp['team']} | Salary: {emp['salary']}")
    print()

def edit_emp():
    search_code = input("Enter Employee Code to update: ")

    for emp in employee_list:
        if emp["code"] == search_code:
            emp["name"] = input("Update Name: ")
            emp["team"] = input("Update Team: ")
            emp["salary"] = input("Update Salary: ")
            print("✔ Employee record updated\n")
            return

    print("Employee code not found\n")

def remove_emp():
    search_code = input("Enter Employee Code to remove: ")

    for emp in employee_list:
        if emp["code"] == search_code:
            employee_list.remove(emp)
            print("✔ Employee removed from records\n")
            return

    print("Employee code not found\n")

def start_app():
    print("Welcome to Employee Management App\n")

    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        user_option = input("Choose an option: ")

        if user_option == "1":
            add_emp()
        elif user_option == "2":
            show_all_emp()
        elif user_option == "3":
            edit_emp()
        elif user_option == "4":
            remove_emp()
        elif user_option == "5":
            print("Application closed. Thank you!")
            break
        else:
            print("Invalid option. Try again.\n")

start_app()

