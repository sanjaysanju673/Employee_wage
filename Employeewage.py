'''
    @Author: v sanjay kumar
    @Date: 2024-07-04 11:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-04 11:00:30
    @Title : Employee wage problem
'''

import random

class Employee:
    def __init__(self, name):
        self.name = name

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

    def calculate_monthly_wage(self, company):
        """
        Calculate the total monthly wage for an employee for a given company.

        Parameters:
        - company: Company object containing wage parameters

        Returns:
        - Total monthly wage of the employee
        """
        total_hours = 0
        total_days = 0
        total_wage = 0
        monthly_wages=[]
        while total_hours <= company.max_working_hours and total_days < company.max_working_days:
            attendance = self.check_attendance()
            daily_wage = company.calculate_daily_wage(attendance)
            monthly_wages.append(daily_wage)
            total_wage += daily_wage
            if attendance == 'full time':
                total_hours += company.full_time_hours
            elif attendance == 'part time':
                total_hours += company.part_time_hours
            total_days += 1
        print("Employee monthly wages list",monthly_wages)
        return total_wage

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

def main():
    """
    Display the menu and handle user choices.
    """
    companies = {
        "tcs": Company("tcs", 20, 20, 100),
        "apple": Company("apple", 25, 22, 120),
        "techmahindra": Company("techmahindra", 22, 18, 90),
    }

    while True:
        try:
            print("Menu:")
            print("1. Calculate Monthly Wage for Company")
            print("2. Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                name = input("Enter the name of the employee: ")
                employee = Employee(name)
                company_name = input("Enter the company name (tcs, techmahindra, apple): ")

                if company_name in companies.keys():
                    company = companies[company_name]
                    total_wage = employee.calculate_monthly_wage(company)
                    print(employee.calculate_monthly_wage(company))
                    print(f"{name} employee monthly wage for {company_name} is {total_wage}")
                else:
                    print("Invalid company name. Please enter a valid company.")

            elif choice == 2:
                print("Exiting the program.")
                break

            else:
                print("Invalid input. Please choose a valid option.")

        except ValueError:
            print("Error: Please enter a numeric value.")

if __name__ == '__main__':
    main()
