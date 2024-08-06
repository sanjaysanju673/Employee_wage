'''
    @Author: v sanjay kumar
    @Date: 2024-07-30 02:30:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-30 02:30:30
    @Title : Employee wage problem
'''
import random
def check_attendance(self):
        """
        Check the attendance for an employee.

        Returns:
        - 'full time' if employee is present full time
        - 'part time' if employee is present part time
        """
        attendance = random.randint(0, 2)
        if attendance == 1:
            return 'full time'
        elif attendance == 2:
            return 'part time'
        else:
            return 'absent'

def daily_wage():
    
    if (check_attendance()=='full time'):
        full_hours = 8
    elif(check_attendance() =='absent'):
        full_hours =0
    Wage_per_hour =20
    
    
    return Wage_per_hour*full_hours
def part_time():
    if(check_attendance() == 'part time'):
        part_hour = 4
    wage_hour =20
    return wage_hour*part_hour


def main():
    print("The employee is ",check_attendance())
    print("daily wage",daily_wage())
    print("part Time wage",part_time())

if __name__ =='__main__':
     main()


