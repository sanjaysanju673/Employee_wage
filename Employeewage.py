'''
    @Author: v sanjay kumar
    @Date: 2024-07-30 11:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-30 11:00:30
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

def main():
    print("The employee is ",check_attendance())


if __name__ =='__main__':
     main()