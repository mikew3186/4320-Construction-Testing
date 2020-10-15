import pytest
import System
import json

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'



#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'saab'
    password =  'boomr345'
    grading_system.login(username,password)

def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False


def test_change_grade(grading_system):
    grading_system.login(profUser,profPass) #login as Staff
    grade = 15
    grading_system.usr.change_grade('akend3','databases',assignment,grade)
    with open('Data/users.json','r') as f:
        data = json.load(f)

    if data['akend3']['courses']['databases'][assignment]['grade'] != grade: #check if the element is correct
        assert False

def test_create_assignment(grading_system):
    grading_system.login(profUser,profPass)#login as Staff
    with open('Data/courses.json','r') as f:
        data = json.load(f)
    initialAssignmentSize = len(data['cloud_computing']['assignments'])
    grading_system.usr.create_assignment('assignmentTest', '10/18/20', 'cloud_computing')

    with open('Data/courses.json','r') as f:
        data = json.load(f)
    
    newAssignmentSize = len(data['cloud_computing']['assignments'])
    if initialAssignmentSize == newAssignmentSize:#if sizes are the same after a new assignment has been added, assert False
        assert False
    #test if a new assignment exists


def test_add_student(grading_system):
    grading_system.login(profUser,profPass) #login as Professor
    courseCheck = 'databases'
    grading_system.usr.add_student('yted91',courseCheck)
    with open('Data/users.json','r') as f:
        data = json.load(f)

    successfullyAdded = False
    for i in data['yted91']['courses']:# try to find databases in the user's course list
        if i == courseCheck:
            successfullyAdded = True #if databases is found, the course was successfully added

    assert successfullyAdded


def test_drop_student(grading_system):
    grading_system.login(profUser,profPass) #login as Professor
    grading_system.usr.drop_student('hdjsr7','databases')
    with open('Data/users.json','r') as f:
        data = json.load(f)
    successfullyDropped = True
    for i in data['hdjsr7']['courses']:
        if i == 'databases':#if databases wasn't dropped, set successfullyDropped to False, test failed
            successfullyDropped = False

    assert successfullyDropped
    

def test_submit_assignment(grading_system):
    grading_system.login('akend3','123454321')
    testDate = '10/08/20'
    grading_system.usr.submit_assignment('databases',assignment,'This is a test submission',testDate)
    with open('Data/users.json','r') as f:
        data = json.load(f)
    if data['akend3']['courses']['databases'][assignment]['submission_date'] != testDate:
        assert False

def test_check_ontime(grading_system):
    grading_system.login('akend3','123454321')
    testing = grading_system.usr.check_ontime('03/01/20','03/02/20')
    assert testing


def test_check_grades(grading_system):
    grading_system.login('akend3','123454321')
    gradeList = grading_system.usr.check_grades('databases')
    with open('Data/users.json','r') as f:
        data = json.load(f)
    if gradeList[0][1] != data['akend3']['courses']['databases']['assignment1']['grade']: #if the first grades aren't equal, assert False
        assert False

def test_view_assignments(grading_system):
    grading_system.login('akend3','123454321')
    assignmentList = grading_system.usr.view_assignments('databases')
    with open('Data/courses.json','r') as f:
        data = json.load(f)
    
    if len(assignmentList) != len(data['databases']['assignments']):#if the lengths don't match up, the test should fail
        assert False



#Last five tests

#tests whether or not a new username is valid
def test_new_username(grading_system):
    with open('Data/users.json','r') as f:
        data = json.load(f)

    newUsername = 'saab' #trying to see if a new user could have a username of saab
    validUsername = True
    for i in data:
        if i == newUsername:
            validUsername = False #if someone else has the username, that new username is not valid
    
    assert validUsername


#tests whether or not a user has any courses (i.e. is a student in a course or is a professor teaching a course?)
def test_enrollment(grading_system):
    with open('Data/users.json','r') as f:
        data = json.load(f)


    userTest = 'ttt' #replacing this with a valid username (e.g. akend3) will yield a test pass
    if len(data[userTest]['courses']) < 1: #if the user has a relation to at least one course
        assert False

#tests if a professor is teaching a certain course
def test_if_professor_teaches_course(grading_system):
    with open('Data/users.json','r') as f:
        data = json.load(f)

    testCourse = 'cloud_computing'

    teachesCourse = False
    for i in data[profUser]['courses']:#currently will fail because user 'goggins' doesn't teach the testCourse
        if i == testCourse:
            teachesCourse = True
    
    assert teachesCourse


#tests if 
#def test_(grading_system):

#tests if 
#def test_(grading_system):

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
