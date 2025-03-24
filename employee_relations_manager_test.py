import employee
import employee_manager
import relations_manager
import datetime

def test_john_doe_birthday_leader():
    output = False
    rm = relations_manager.RelationsManager()
    employees = rm.get_all_employees()
    
    for e in employees:
        if e.first_name == "John" and e.last_name == "Doe" and e.birth_date == datetime.date(1970, 1, 31) and rm.is_leader(e):
            output = True
    assert output == True

def test_john_doe_team_myrta_jettie():
    output = False
    rm = relations_manager.RelationsManager()
    employee = rm.get_employee_by_name("John", "Doe") 
    team_members = rm.get_team_members(employee)
    for tm in team_members:
        emp = rm.get_employee_by_id(tm)
        if emp.first_name == "Myrta" or emp.first_name == "Jettie":
            if emp.last_name == "Torkelson" or emp.last_name == "Lynch":
                output = True
    assert output ==  True

def test_andre_not_doe_team_member():
    output = True
    rm = relations_manager.RelationsManager()
    doe = rm.get_employee_by_name("John", "Doe")
    team_members = rm.get_team_members(doe)
    for tm in team_members:
        emp = rm.get_employee_by_id(tm)
        if emp.first_name == "Tomas" and emp.last_name == "Andre":
            output = False
    assert output == True
    
def test_gretchen_watford_salary_4000():
    output = False
    rm = relations_manager.RelationsManager()
    gretchen = rm.get_employee_by_name("Gretchen", "Watford")
    if gretchen.base_salary == 4000:
        output = True
    assert output == True

def test_no_jude_overcash():
    output = True
    rm = relations_manager.RelationsManager()
    employees = rm.get_all_employees()
    for e in employees:
        if e.first_name == "Jude" and e.last_name == "Overcash":
            output = False
    assert output == True


