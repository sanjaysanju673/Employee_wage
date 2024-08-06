import random

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

def daily_wage(name, attendance):
    """
    Calculate the daily wage for a full-time employee based on attendance.

    Parameters:
    - name: Name of the employee
    - attendance: Attendance status of the employee

    Returns:
    - Daily wage of the employee
    """
    full_hours = 8 if attendance == 'full time' else 0
    wage_per_hour = 20
    wage = wage_per_hour * full_hours
    print(f'{name} wage is {wage}')
    return wage

def part_time(name, attendance):
    """
    Calculate the daily wage for a part-time employee based on attendance.

    Parameters:
    - name: Name of the employee
    - attendance: Attendance status of the employee

    Returns:
    - Part-time wage of the employee
    """
    part_hours = 4 if attendance == 'part time' else 0
    wage_per_hour = 20
    wage = wage_per_hour * part_hours
    print(f'{name} wage is {wage}')
    return wage

def wage_per_month(name):
    """
    Calculate the total monthly wage for an employee.

    Parameters:
    - name: Name of the employee

    Returns:
    - Total monthly wage of the employee
    """
    total_month_wage = 0
    for _ in range(20):
        attendance = check_attendance()
        if attendance == 'full time':
            total_month_wage += daily_wage(name, attendance)
        elif attendance == 'part time':
            total_month_wage += part_time(name, attendance)
    print(f"{name} employee monthly wage is {total_month_wage}")
    return total_month_wage

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
            print("5. Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                attendance = check_attendance()
                print(f"Attendance: {attendance}")

            elif choice == 2:
                name = input("Enter the name of the employee: ")
                attendance = check_attendance()
                daily_wage(name, attendance)

            elif choice == 3:
                name = input("Enter the name of the employee: ")
                attendance = check_attendance()
                part_time(name, attendance)

            elif choice == 4:
                name = input("Enter the name of the employee: ")
                wage_per_month(name)

            elif choice == 5:
                print("Exiting the program.")
                break

            else:
                print("Invalid input. Please choose a valid option.")

        except ValueError:
            print("Error: Please enter a numeric value.")

if __name__ == '__main__':
    main()
