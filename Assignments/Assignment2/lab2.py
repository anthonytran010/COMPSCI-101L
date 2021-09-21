########################################################################
##
## CS 101 Lab
## Program #1
## Name Anthony Tran
## Email attnwr@umsystem.edu
##
## PROBLEM : Calcukating Grades
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
print('**** Welcome to the LAB grade calculator! ****')
print('')
name = input('Who are we calculating grades for> ==>')
print('')
lab = int(input('Enter the Labs grade? ==>'))
if lab < 0:
    print('The lab value should have been zero or greater. It has been changed to zero.')
    lab = 0
if lab > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    lab = 100
print('')
exam = int(input('Enter the EXAM grade? ==>'))
if exam < 0:
    print('The exam value should have been zero or greater. It has been changed to zero.')
    exam = 0
if exam > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
print('')
attend = int(input('Enter the Attendance grade? ==>'))
if attend < 0:
    print('The attendance value should have been zero or less. It has been changed to zero.')
    attend = 0
if attend > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    attend = 100
print('')
grade = (lab*.7) + (exam*.2) + (attend*.1)
letter =()
if grade <= 100 and grade >= 90:
    letter = 'A'
if grade <= 89 and grade >= 80:
    letter = 'B'
if grade <= 79 and grade >= 70:
    letter = 'C'
if grade <= 69 and grade >= 60:
    letter = 'D'
if grade <= 59:
    letter = 'F'
print('The weighted grade for', name, 'is', grade)
print(name, 'has a letter grade of', letter)
print('')
print('**** Thanks for using the Lab grade calculator ****')