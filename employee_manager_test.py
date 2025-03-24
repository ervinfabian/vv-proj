import employee
import employee_manager
import relations_manager
import datetime

def test_first():
    rm = relations_manager.RelationsManager()
    em = employee_manager.EmployeeManager(rm)
    rm.add_employee("employee", "seven", 1000, 
    datetime.date(1980, 12, 29), datetime.date(1998, 10, 10))
    employee = rm.get_employee_by_id(7)
    print("first test**************************************************")
    output = em.calculate_salary(employee)
    assert output == 3700

def test_second():
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
    assert output == 4300

def test_email():
    rm = relations_manager.RelationsManager()
    em = employee_manager.EmployeeManager(rm)
    rm.add_employee("employee", "seven", 1000, datetime.date(1980, 12, 29), datetime.date(1998, 10, 10))
    rm.add_employee("employee", "eight", 2000, datetime.date(1980, 1,1), datetime.date(2008, 10, 10))
    rm.add_employee("employee", "nine", 1000, datetime.date(1978, 1, 1), datetime.date(1998, 10, 19))
    rm.add_employee("employee", "ten", 1000, datetime.date(1987, 1, 1), datetime.date(1986, 1, 1))
    rm.teams.update({8: [7, 9, 10]})
    em.calculate_salary_and_send_email(rm.get_employee_by_id(7))
    

