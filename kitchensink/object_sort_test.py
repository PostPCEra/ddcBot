#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

d1= [ {'name': 'gitu', 'grade': 93}, {'name': 'manju', 'grade': 89}, {'name': 'charvi', 'grade': 80},
     {'name': 'bani', 'grade': 78}
     ]

ltypes = [str(type(x)) for x in d1]
if len(set(ltypes)) != 1:
    print('error not same type')
elif ltypes[0] != "<class 'dict'>":
    print('error not DiCT')

print(d1)
d2 = []
for row in d1:
    if row['grade'] >= 80:
        d2.append(row)
print(d2)

# ---------------- sorting of List and List of dict
l1 = [ 4, 5, 9, 9.1, 2]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

l1 = [ 'gitu', 'bani', 'manju', 'charvi']
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

# ----- no soring of List of Dict,  only Filter of List of Dict ....
def doit(row1, row2):
    return False
    v1, v2 = row1['grade'], row2['grade']
    return  v2 - v1
    if isinstance(v1, str):
        return v1 > v2
    else:
        return v1 - v2

d2 = sorted(d1, key= functools.cmp_to_key(doit), reverse=True)
print(d1)
print(d2)

# -------------------------  Objects --------------------
# http://hplgit.github.io/primer.html/doc/pub/class/._class-solarized002.html
class Student(object):
    def __init__(self, name, age, grade=0):
        self.name = name
        self.age = age
        self.grade = grade

    def add_age(self, age):
        self.age = age

    def add_grade(self, grade):
        self.grade = grade

    def print(self, attr=False):
        s = '{}, {}, {}'.format(self.name, self.age, self.grade)
        if attr:
            s = 'Name, age, grade: ' + s
        print(s)

s1 = Student('Hans Hanson', 11, 83)
s2 = Student('Rand Paul', 10)
s2.add_grade(99)
s3 = Student('Ann B.', 12)

grade_book = [s1, s2, s3]

type(s1.age)
def student_compare(o1, o2):

    if (o1.name > o2.name):
        ret = 1
    elif (o1.name < o2.name):
        ret = -1
    else:
        ret = 0
    return 0
    #return o1.age - o2.age


sortbook = sorted(grade_book, key=functools.cmp_to_key(student_compare))


for stu in sortbook:
    stu.print()