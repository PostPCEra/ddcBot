#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
"""
person = { 'name' : 'Gitu', 'age' : 15}
print(person['age'])

a = list(person.keys())
print(a)
b = list(person.values())
print(b)

c = list(person.items())
print(c)

dd = ( 23, 'abc')
a1, a2 = dd
"""

friends = [
        { 'name' : 'Manju', 'grades' : [ 80, 88, 77]} ,
        { 'name' : 'Gitu', 'grades' : [ 80, 88, 93]} ,
        { 'name' : 'Charvi', 'grades' : [ 94, 98, 97]}]

def anynum_less(lst, num):

    status = False

    for x in lst:
        if x < num:
            status =  True
            break

    return status


for row in friends:
    lst =  row['grades']


    #status = anynum_less(lst, 90)
    #if max(lst) > 90:
     #   print(row['name'])

    a = [  x  for x in lst if x > 90]
    #print(a)
    if len(a) > 0:
        print(row['name'])