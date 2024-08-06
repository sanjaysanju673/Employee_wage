
'''
   @Author: v sanjay kumar
   @Date: 2024-07-19 1:10:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-19 1:10:30
   @Title : program to Employeewage problem

'''



import random
print("WellCome to Employee wage Program ")
class Employee:
    def __init__(self, name):
        self.name = name
        self.total_wage = 0

    @staticmethod
    def check_attendance():
        """
        Check the attendance for an employee.

        Returns:
        - 'full time' if employee is present full time
        - 'part time' if employee is present part time
        - 'absent' if employee is absent
        """
        attendance = random.randint(0, 2)
        if attendance == 1:
            return 'full time'
        elif attendance == 2:
            return 'part time'
        else:
            return 'absent'

class Company:
    def __init__(self, name, wage_per_hour, max_working_days, max_working_hours):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_time_hours = 8
        self.part_time_hours = 4
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def calculate_daily_wage(self, attendance):
        """
        Calculate the daily wage for an employee based on attendance.

        Parameters:
        - attendance: Attendance status of the employee

        Returns:
        - Daily wage of the employee
        """
        if attendance == 'full time':
            hours = self.full_time_hours
        elif attendance == 'part time':
            hours = self.part_time_hours
        else:
            hours = 0
        wage = self.wage_per_hour * hours
        return wage

class EmployeeManager:
    def __init__(self, company_builder):
        self.company_builder = company_builder

    def manage_employee(self):
        """
        Manage employee operations (Add, Delete, Update).
        Parameters:none
        returns :None
        """
        while True:
            print("\nEmployee Management Menu:")
            print("1. Add Employee")
            print("2. Delete Employee")
            print("3. Update Employee")
            print("4. Go Back")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                employee_name = input("Enter the name of the employee to add: ")
                self.add_employee(employee_name)

            elif choice == 2:
                employee_name = input("Enter the name of the employee to delete: ")
                self.delete_employee(employee_name)

            elif choice == 3:
                employee_name = input("Enter the current name of the employee: ")
                new_name = input("Enter the new name of the employee: ")
                self.update_employee(employee_name, new_name)

            elif choice == 4:
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def add_employee(self, employee_name):
        '''the method is used to the add the employee to company
        parameters: employee_name
        return :none 
        ''' 
        
        if employee_name not in self.company_builder.employees:
            employee = Employee(employee_name)
            self.company_builder.add_employee(employee)
            print(f"Employee {employee_name} added successfully.")
        else:
            print(f"Employee {employee_name} already exists.")

    def delete_employee(self, employee_name):
         '''the method is used to the delete the employee to company
        parameters: employee_name
        return :none 
        ''' 
         
         self.company_builder.delete_employee(employee_name)

    def update_employee(self, employee_name, new_name):
          '''the method is used to the upadate the employee to company
        parameters: employee_name,new_name
        return :none '''
          self.company_builder.update_employee(employee_name, new_name)

    def calculate_monthly_wage(self, employee_name):
        '''the method is used to the calculate monthly wage employee to company

        parameters: employee_name

        return :none '''
        if employee_name in self.company_builder.employees:
            employee = self.company_builder.employees[employee_name]
            total_wage, monthly_wages = self.company_builder.calculate_monthly_wage(employee)
            print(f"{employee_name}'s monthly wage is {total_wage}")
            print(f"Daily wages: {monthly_wages}")
        else:
            print(f"Employee {employee_name} does not exist.")

class EmpWageBuilder:
    def __init__(self, company):
        self.company = company
        self.employees = {}
        self.employee_manager = EmployeeManager(self)

    def add_employee(self, employee):
        '''the method is used to the add the  employee to company

        parameters: employee_name

        return :none '''
        if employee.name not in self.employees:
            self.employees[employee.name] = employee
        else:
            print(f"Employee {employee.name} already exists.")

    def delete_employee(self, employee_name):
        '''
        the method is used to the delete employee to company

        parameters: employee_name

        return :none 
        '''
        if employee_name in self.employees:
            del self.employees[employee_name]
            print(f"Employee {employee_name} deleted successfully.")
        else:
            print(f"Employee {employee_name} does not exist.")

    def update_employee(self, employee_name, new_name):
        '''the method is used to the update the  employee name to the company

        parameters: employee_name

        return :none '''
        if employee_name in self.employees:
            employee = self.employees[employee_name]
            employee.name = new_name
            self.employees[new_name] = self.employees.pop(employee_name)
            print(f"Employee {employee_name} updated to {new_name}.")
        else:
            print(f"Employee {employee_name} does not exist.")

    def calculate_monthly_wage(self, employee):
        total_hours = 0
        total_days = 0
        total_wage = 0
        monthly_wages = []
        while total_hours <= self.company.max_working_hours and total_days < self.company.max_working_days:
            attendance = employee.check_attendance()
            daily_wage = self.company.calculate_daily_wage(attendance)
            monthly_wages.append(daily_wage)
            total_wage += daily_wage
            if attendance == 'full time':
                total_hours += self.company.full_time_hours
            elif attendance == 'part time':
                total_hours += self.company.part_time_hours
            total_days += 1

        employee.total_wage = total_wage
        return total_wage, monthly_wages

    def display_employee_wages(self):
        '''the method is used to the display  the employee wage to company
        parameters:none
        return :none '''
        for employee_name, employee in self.employees.items():
            print(f"{employee_name}: {employee.total_wage}")

    def display_company_details(self):
        '''the method is used to the display  company details.
        parameters:none
        return :none '''
        print(f"Company Name: {self.company.name}")
        print(f"Wage per Hour: {self.company.wage_per_hour}")
        print(f"Max Working Days: {self.company.max_working_days}")
        print(f"Max Working Hours: {self.company.max_working_hours}")
        print("\nEmployee Details:")
        self.display_employee_wages()

def add_company(companies, builders):
    """
    Add a new company.

    Parameters:
    - companies: Dictionary of existing companies
    - builders: Dictionary of existing builders
    """
    name = input("Enter company name: ")
    wage_per_hour = int(input("Enter wage per hour: "))
    max_working_days = int(input("Enter maximum working days per month: "))
    max_working_hours = int(input("Enter maximum working hours per month: "))
    
    new_company = Company(name, wage_per_hour, max_working_days, max_working_hours)
    companies[name] = new_company
    builders[name] = EmpWageBuilder(new_company)
    print(f"Company {name} added successfully.")

def delete_company(companies, builders):
    """
    Delete an existing company.

    Parameters:
    - companies: Dictionary of existing companies
    - builders: Dictionary of existing builders
    """
    name = input("Enter company name to delete: ")
    if name in companies:
        del companies[name]
        del builders[name]
        print(f"Company {name} deleted successfully.")
    else:
        print(f"Company {name} does not exist.")

def modify_company(companies, builders):
    """
    Modify the details of an existing company.

    Parameters:
    - companies: Dictionary of existing companies
    - builders: Dictionary of existing builders
    """
    name = input("Enter company name to modify: ")
    if name in companies:
        wage_per_hour = int(input("Enter new wage per hour: "))
        max_working_days = int(input("Enter new maximum working days per month: "))
        max_working_hours = int(input("Enter new maximum working hours per month: "))
        
        company = companies[name]
        company.wage_per_hour = wage_per_hour
        company.max_working_days = max_working_days
        company.max_working_hours = max_working_hours
        print(f"Company {name} modified successfully.")
    else:
        print(f"Company {name} does not exist.")

def main():
    """
    Display the menu and handle user choices.
    """
    companies = {}
    builders = {}

    while True:
        try:
            print("\nMenu:")
            print("1. Calculate Monthly Wage for Employee")
            print("2. Add Company")
            print("3. Delete Company")
            print("4. Modify Company")
            print("5. Manage Employees")
            print("6. Display Company and Employee Details")
            print("7. Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                name = input("Enter the name of the employee: ")
                company_name = input("Enter the company name: ")

                if company_name in builders:
                    builder = builders[company_name]
                    builder.employee_manager.calculate_monthly_wage(name)
                else:
                    print("Invalid company name. Please enter a valid company.")

            elif choice == 2:
                add_company(companies, builders)

            elif choice == 3:
                delete_company(companies, builders)

            elif choice == 4:
                modify_company(companies, builders)

            elif choice == 5:
                company_name = input("Enter the company name to manage employees: ")
                if company_name in builders:
                    builder = builders[company_name]
                    builder.employee_manager.manage_employee()
                else:
                    print("Invalid company name. Please enter a valid company.")

            elif choice == 6:
                company_name = input("Enter the company name to display details: ")
                if company_name in builders:
                    builder = builders[company_name]
                    builder.display_company_details()
                else:
                    print("company name company does not exist. Please enter a valid company.")

            elif choice == 7:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
