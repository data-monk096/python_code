import csv
import os
import re


# Create class Employee
class Employee:
    def __init__(self, emp_id, name, dept, join_date, status, salary):
        # Initialize the Employee object with provided attributes
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.join_date = join_date
        self.status = status
        self.salary = salary

    def save(self, csv_file='employee.csv'):
        # Check if the CSV file already exists
        is_file_exists = os.path.isfile(csv_file)

        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            # Write header row if the file is newly created
            if not is_file_exists:
                writer.writerow(["Emp_ID", "Name", "Dept", "JoinDate", "Status", "Salary"])

            # Write the employee details to the CSV file
            writer.writerow([self.emp_id, self.name, self.dept, self.join_date, self.status, self.salary])

    def __str__(self):
        # String representation of the Employee object
        return f"Employee ID: {self.emp_id}, Name: {self.name},\
         Department: {self.dept}, Join Date: {self.join_date},\
               Status: {self.status}, Salary: {self.salary}"


def validate_emp_id(emp_id):
    # Check if emp_id has more than 6 characters
    if len(emp_id) > 6:
        return False
    return True


def validate_name_dept(value):
    # Check if value contains any numeric characters
    if re.search(r'\d', value):
        return False
    return True


def validate_salary(value):
    # Check if value is a numeric value
    try:
        float(value)
        return True
    except ValueError:
        return False


def validate_join_date(join_date):
    # Check if join_date is in the correct date format
    if re.match(r'\d{4}-\d{2}-\d{2}$', join_date):
        return True
    return False


def get_details():
    while True:
        empire = input("Enter employee ID (not more than 6 characters): ")
        if not validate_emp_id(empire):
            print("Invalid employee ID. Please enter a maximum of 6 characters.")
        else:
            break

    while True:
        na = input("Enter name: ")
        if not validate_name_dept(na):
            print("Invalid name. Name should not contain numeric characters.")
        else:
            break

    while True:
        de = input("Enter department: ")
        if not validate_name_dept(de):
            print("Invalid department. Department should not contain numeric characters.")
        else:
            break

    while True:
        join_d = input("Enter join date (YYYY-MM-DD): ")
        if not validate_join_date(join_d):
            print("Invalid join date. Please enter the date in the format YYYY-MM-DD.")
        else:
            break

    sta = input("Enter status: ")

    while True:
        sal = input("Enter salary: ")
        if not validate_salary(sal):
            print("Invalid salary. Please enter a numeric value.")
        else:
            break

    # Create an Employee object and save the details to a CSV file
    Employee(empire, na, de, join_d, sta, sal).save(csv_file="employee_data.csv")


# Call function to save as csv
get_details()
