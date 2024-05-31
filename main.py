import datetime
import kaneki
# import functions from modules
from application.salary import calculate_salary
from application.db.people import get_employees
# or import all modules
# from application import salary as sal
# from application.db import people as pe

if __name__ == '__main__':
    print(datetime.datetime.now())
    print(calculate_salary())
    print(get_employees())
    # kaneki.torture()

