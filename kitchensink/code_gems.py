#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# -------------------  Code Gems from web ---------------------------
#
# -------------------  *****************  ---------------------------

# https://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-a-list
l = [1, 2, 3, 4, 4, 5, 5, 6, 1]
uniq = set([x for x in l if l.count(x) > 1])
# {1, 4, 5}


# https://stackoverflow.com/questions/43698531/sorting-a-zipped-object-in-python-3
l1 = [3, 9, 2, 24, 1, 6]
l2 = ['a', 'b', 'c', 'd', 'e']
zp = zip(l1, l2)

slist = sorted(zp, key=lambda p: p[1])  # sorting  based on the values of y in each (x,y) pair , for x sort use p[0]
# [(3, 'a'), (9, 'b'), (2, 'c'), (24, 'd'), (1, 'e')]


# https://stackoverflow.com/questions/16628088/euclidean-algorithm-gcd-with-multiple-numbers
from fractions import gcd
lis = [3, 6, 9, 12]
result = gcd(*lis[:2])  # get the gcd of first two numbers ( unpack list as parameters with * )
if len(lis) >2:
    for x in lis[2:]:    # now iterate over the list starting from the 3rd element
        result = gcd(result,x)
print(result)
