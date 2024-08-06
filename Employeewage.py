'''
    @Author: v sanjay kumar
    @Date: 2024-07-03 02:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-03 02:00:30
    @Title : Employee wage problem
'''

import random

class Employee:
    def __init__(self, name):
        self.name = name
        self.wage_per_hour = 20
        self.full_time_hours = 8
        self.part_time_hours = 4
        self.total_hours = 0
        self.total_days = 0
        self.monthly_wage = 0

    def check_attendance(self):
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
        print(f'{self.name} wage is {wage}')
        return wage

    def calculate_monthly_wage(self):
        """
        Calculate the total monthly wage for an employee.
        """
        for _ in range(20):
            attendance = self.check_attendance()
            daily_wage = self.calculate_daily_wage(attendance)
            self.monthly_wage += daily_wage
        print(f"{self.name} employee monthly wage is {self.monthly_wage}")
        return self.monthly_wage

    def wage_per_condition(self):
        """
        Calculate the total monthly wage for an employee based on conditions.
        """
        while self.total_hours <= 100 and self.total_days <= 20:
            attendance = self.check_attendance()
            if attendance == 'full time':
                self.total_hours += self.full_time_hours
                wage = self.calculate_daily_wage(attendance)
            elif attendance == 'part time':
                self.total_hours += self.part_time_hours
                wage = self.calculate_daily_wage(attendance)
            else:
                wage = 0
            self.monthly_wage += wage
            self.total_days += 1
        print('Employee monthly wage', self.monthly_wage)
        return self.monthly_wage


def main():
    """
    Display the menu and handle user choices.
    """
    while True:
        try:
            print("Menu:")
            print("1. Check Attendance")
            print("2. Calculate Full-Time Daily Wage")
            print("3. Calculate Part-Time Daily Wage")
            print("4. Calculate Monthly Wage")
            print("5. Calculate Wage Per Condition")
            print("6. Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                employee = Employee(input("Enter the name of the employee: "))
                attendance = employee.check_attendance()
                print(f"Attendance: {attendance}")

            elif choice == 2:
                employee = Employee(input("Enter the name of the employee: "))
                attendance = employee.check_attendance()
                employee.calculate_daily_wage(attendance)

            elif choice == 3:
                employee = Employee(input("Enter the name of the employee: "))
                attendance = employee.check_attendance()
                employee.calculate_daily_wage(attendance)

            elif choice == 4:
                employee = Employee(input("Enter the name of the employee: "))
                employee.calculate_monthly_wage()

            elif choice == 5:
                employee = Employee(input("Enter the name of the employee: "))
                employee.wage_per_condition()

            elif choice == 6:
                print("Exiting the program.")
                break

            else:
                print("Invalid input. Please choose a valid option.")

        except ValueError:
            print("Error: Please enter a numeric value.")

if __name__ == '__main__':
    main()
