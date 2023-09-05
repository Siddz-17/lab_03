class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
class EmployeeDatabase:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def search_by_age(self, age):
        results = [emp for emp in self.employees if emp.age == age]
        return results
    def search_by_name(self, name):
        results = [emp for emp in self.employees if emp.name == name]
        return results
    def search_by_salary(self, operator, salary):
        if operator == ">":
            results = [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<":
            results = [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">=":
            results = [emp for emp in self.employees if emp.salary >= salary]
        elif operator == "<=":
            results = [emp for emp in self.employees if emp.salary <= salary]
        else:
            results = []
        return results
def main():
    database = EmployeeDatabase()
    employee1 = Employee("161E90", "Raman", 41, 56000)
    employee2 = Employee("161F91", "Himadri", 38, 67500)
    employee3 = Employee("161F99", "Jaya", 51, 82100)
    employee4 = Employee("171E20", "Tejas", 30, 55000)
    employee5 = Employee("171G30", "Ajay", 45, 44000)
    database.add_employee(employee1)
    database.add_employee(employee2)
    database.add_employee(employee3)
    database.add_employee(employee4)
    database.add_employee(employee5)
    print("Search options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        age = int(input("Enter the age to search: "))
        results = database.search_by_age(age)
    elif choice == 2:
        name = input("Enter the name to search: ")
        results = database.search_by_name(name)
    elif choice == 3:
        operator = input("Enter the operator (> or < or >= or <=): ")
        salary = int(input("Enter the salary to search: "))
        results = database.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    if results:
        print("Search Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")
if __name__ == "__main__":
    main()
