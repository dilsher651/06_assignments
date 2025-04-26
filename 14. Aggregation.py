class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation: Stores independent Employee objects
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"\nEmployees in {self.dept_name} department:")
        for emp in self.employees:
            emp.display_info()

# Create independent Employee objects
emp1 = Employee("John Doe", "E1001")
emp2 = Employee("Jane Smith", "E1002")

# Create a Department
hr_dept = Department("Human Resources")

# Add employees to department (aggregation)
hr_dept.add_employee(emp1)
hr_dept.add_employee(emp2)

# List department employees
hr_dept.list_employees()

# Employees continue to exist even if department is deleted
del hr_dept
print("\nAfter department deletion:")
emp1.display_info()  # Still accessible