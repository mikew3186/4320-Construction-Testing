# Exercise 07.1 - Construction and Testing
## CS4320/7320 Software Engineering


Mike Weiss

mjwcbc

##07-Construction-Testing

##About my submission

If you go into the exercises directory, you will find the python files, including 'my_test.py'. This is the file with all 15 of my tests. This file should be able to be ran by running 'pytest' in the terminal. However, the pycache folder may need to be deleted in order for the files to run successfully.


There are ten tests that fail. My five additional customs tests all fail, as well as tests for the following:

login

check_ontime

check_grades

view_assignments

add_student


These failed tests can be made to work if a parameter is changed. For example, in test_add_student, modifying the courseCheck variable and assigning it an actual course name (e.g. 'databases') will make the test pass, so my implementation of the underlying tests should not be an issue. Likewise, providing a valid username and password in test_login will make the test pass.


Also, the first two tests (login and check_password) are derived from the code that was posted to the Slack channel. These tests worked, so I used them. They were useful in determining how to approach this assignment and how to create the remaining tests, since I have more or less never used Python.
