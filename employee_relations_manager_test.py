import employee
import employee_manager
import relations_manager
import datetime

def test_john_doe_birthday_and_if_is_leader():
    # Check if there is a team leader called John Doe whose birthdate is 31.01.1970.

    output = False
    rm = relations_manager.RelationsManager()
    employees = rm.get_all_employees()
    
    for e in employees:
        if e.first_name == "John" and e.last_name == "Doe" and e.birth_date == datetime.date(1970, 1, 31) and rm.is_leader(e):
            output = True
    assert output == True, "There is no team leader called John Doe, with 31.01.1970 birthdate"

    # If the test is not passed, there is no team leader called John Doe whose birthdate is 31.01.1970

def test_myrta_and_jettie_in_john_doe_team():
    # Check if John Doe’s team members are Myrta Torkelson and Jettie Lynch.

    output = False
    rm = relations_manager.RelationsManager()
    employee = rm.get_employee_by_name("John", "Doe") 
    team_members = rm.get_team_members(employee)
    number_of_correct_employees = 0
    for tm in team_members:
        emp = rm.get_employee_by_id(tm)
        if emp.first_name == "Myrta" and emp.last_name == "Torkelson":
            number_of_correct_employees = number_of_correct_employees + 1
        if emp.first_name == "Jettie" and emp.last_name == "Lynch":
            number_of_correct_employees = number_of_correct_employees + 1
    if number_of_correct_employees == 2:
        output = True

    assert output ==  True, "Jettie Lynch and Myrta Torkelson are not John Doe's team members"

    # If the test is not passed then 

def test_andre_not_in_doe_team():
    # Make sure that Tomas Andre is not John Doe’s team member.

    output = False
    rm = relations_manager.RelationsManager()
    doe = rm.get_employee_by_name("John", "Doe")
    team_members = rm.get_team_members(doe)
    for tm in team_members:
        emp = rm.get_employee_by_id(tm)
        if emp.first_name == "Tomas" and emp.last_name == "Andre":
            output = True
    assert output == False, "Tomas Andre is John Doe's team member"
    
def test_gretchen_watford_base_salary_equals_4000():
    # Check if Gretchen Walford’s base salary equals 4000$.

    output = False
    rm = relations_manager.RelationsManager()
    gretchen = rm.get_employee_by_name("Gretchen", "Watford")
    if gretchen.base_salary == 4000:
        output = True
    assert output == True, "Gretchen Watford's base salary is not 4000$"

def test_no_jude_overcash_in_database():
    # Make sure that Jude Overcash is not stored in the database.

    output = False
    rm = relations_manager.RelationsManager()
    employees = rm.get_all_employees()
    for e in employees:
        if e.first_name == "Jude" and e.last_name == "Overcash":
            output = True
    assert output == False, "Jude overcash is stored in the database"

def test_if_tomas_andre_is_not_team_leader():
    # Make sure Tomas Andre is not a team leader. 
    # Check what happens if you try to retrieve his team members.

    output = False
    rm = relations_manager.RelationsManager()
    tomas_andre = rm.get_employee_by_name("Tomas", "Andre")
    if rm.is_leader(tomas_andre):
        output = True
    assert output == False
    assert rm.get_team_members(tomas_andre) is None, "Tomas Andre is a team leader"

    
