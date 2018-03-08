#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# -------------------  Python problem Sets to Quiz programming knowledge ---------------------------
#
# ----------------------------------------------------------------------------------------------

# write a function to test weather a given two lists l1 and l2 contain same elements or not
# return True or False ; l1 & l2 are of same length ; l2 is a sorted list
def are_the_lists_same(l1, l2):
    if l2[0] < l2[-1]:
        l1.sort()
    else:
        l1.sort(reverse=True)

    for i, _ in enumerate(l1):
        if l1[i] != l2[i]:
            return False
    return True

    # you can also use  "for i in range(len(l1)):"  ;
    # make a test suite with random num generator with 100 cases ; use 'import timeit' lib and see time difference

# ----------------------------------------------------------------------------------------------
