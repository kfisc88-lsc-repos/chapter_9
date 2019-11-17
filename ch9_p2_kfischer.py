"""
File: ch9_p1_kfischer.py
Resources to manage a student's name and test scores.

EDIT:
Author: Kelley Fischer
Date:   11/16/19
Add code to shuffle and sort a list of students.
"""


from ch9_p1_kfischer import Student
from random import shuffle


student1 = Student('Jerry', 5)
student2 = Student('Ted', 6)
student3 = Student('Kevin', 9)
student4 = Student('Jenna', 5)
student5 = Student('Emily', 9)

msHoneysClass = [student1, student2, student3, student4, student5]

shuffle(msHoneysClass)

for student in msHoneysClass:
    print(student)

msHoneysClass.sort()

for student in msHoneysClass:
    print(student)
