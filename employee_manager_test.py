import employee
import employee_manager
import relations_manager
import datetime

def test_not_team_leader_salary():
    # Check an employee’s salary who is not a team leader 
    # whose hire date is 10.10.1998 and his base salary is 
    # 1000$. Make sure the returned value is 3700$ (1000$ + 20 X 100$).

    rm = relations_manager.RelationsManager()
    em = employee_manager.EmployeeManager(rm)
    rm.add_employee("employee", "seven", 1000, 
    datetime.date(1980, 12, 29), datetime.date(1998, 10, 10))
    employee = rm.get_employee_by_id(7)
    output = em.calculate_salary(employee)
    # expected salary is 1000 + 27 x 100 = 3700
    assert output == 3700, "The salary of the employee is not equal to the expected value"

def test_team_leader_salary():
    # Check an employee’s salary who is a team leader 
    # and his team consists of 3 members. 
    # She was hired on 10.10.2008 and has a base salary of 2000$. 
    # Validate if the returned value is 3600$ (2000$ + 10 X 100$ + 3 X 200$).

    rm = relations_manager.RelationsManager()
    em = employee_manager.EmployeeManager(rm)
    rm.add_employee("employee", "seven", 1000, datetime.date(1980, 12, 29), datetime.date(1998, 10, 10))
    rm.add_employee("employee", "eight", 2000, datetime.date(1980, 1,1), datetime.date(2008, 10, 10))
    rm.add_employee("employee", "nine", 1000, datetime.date(1978, 1, 1), datetime.date(1998, 10, 19))
    rm.add_employee("employee", "ten", 1000, datetime.date(1987, 1, 1), datetime.date(1986, 1, 1))
    rm.teams.update({8: [7, 9, 10]})
    employee = rm.get_employee_by_id(8)
    print(rm.get_team_members(employee))
    output = em.calculate_salary(employee)
    # expected salary is 2000 + 17 x 100 + 3 x 200 = 4300
    assert output == 4300, "The salary of the employee is not equal to the expected value"

def test_calculate_salary_send_email():
    # Make sure that when you calculate the salary and send an email notification, 
    # the respective email sender service is used with the correct 
    # information (name and message). 
    # You can use the setup from the previous test for the employee.

    rm = relations_manager.RelationsManager()
    em = employee_manager.EmployeeManager(rm)
    rm.add_employee("employee", "seven", 1000, datetime.date(1980, 12, 29), datetime.date(1998, 10, 10))
    rm.add_employee("employee", "eight", 2000, datetime.date(1980, 1,1), datetime.date(2008, 10, 10))
    rm.add_employee("employee", "nine", 1000, datetime.date(1978, 1, 1), datetime.date(1998, 10, 19))
    rm.add_employee("employee", "ten", 1000, datetime.date(1987, 1, 1), datetime.date(1986, 1, 1))
    rm.teams.update({8: [7, 9, 10]})
    employee_informations = ()

    employee_informations = em.calculate_salary_and_send_email(rm.get_employee_by_id(8))
    assert employee_informations[0] == "employee" and employee_informations[1] == "eight" and employee_informations[2] == 4300, "the email sender and salary calculator function is not working properly"