##Write a python code that will accept a series of test grades and
##print the total number of students, the average grade, the lowest grade, and the highest
##grade.



TotalStudents = 4 #This is the total number of students in the class
print 'The total number of students is ', TotalStudents #By not including the TotalStudents in the statement, the code will return the result to 4 instead of "TotalStudents"

a=0
b=101
     
FirstGrade=int(raw_input('Enter the first grade ='))
if FirstGrade in range(a,b): ##Range needs to be within 0-101 so that the user will know to go below or over 
    print 'The First Grade is', FirstGrade
else:
    print 'Error Submission'    
SecondGrade=int(raw_input ('Enter the second grade = '))
 
if SecondGrade in range(a,b):
    print 'The Second Grade is', SecondGrade
else:
    print 'Error Submission'
    
ThirdGrade=int(raw_input ('Enter the third grade = '))
if ThirdGrade in range(a,b):
    print 'The Third Grade is', ThirdGrade
else:
    print 'Error Submission'
    
FourthGrade=int(raw_input ('Enter the fourth grade='))

if FourthGrade in range(a,b):
    print 'The Fourth Grade is ', FourthGrade
else:
    print 'Error Submission'

FirstofGrades = FirstGrade + SecondGrade ##Need to declare FirstofGrades since adding elements require 2 items instead of 4

SecondofGrades = ThirdGrade + FourthGrade #Need to declare SecondofGrades since adding elements require 2 items instead of 4

AllofGrades = FirstofGrades + SecondofGrades #Need to declare AllofGrades since adding elements require 2 items instead of 4

AverageTestGrade = AllofGrades // TotalStudents 

print 'The average of test grade is', AverageTestGrade


LowestTestGrade = min(FirstGrade, SecondGrade, ThirdGrade, FourthGrade)
print 'The lowest test grade is', LowestTestGrade


HighestTestGrade = max(FirstGrade, SecondGrade, ThirdGrade, FourthGrade)
print 'The highest test grade is', HighestTestGrade

