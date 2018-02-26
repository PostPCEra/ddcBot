#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# Basic Calculator
# https://stackoverflow.com/questions/1740726/turn-string-into-operator
import operator


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    allops = {"+": operator.add,  # if no operator lib, you can have this as  "+": op1 + op2
              "-": operator.sub,
              '*': operator.mul,
              '/': operator.truediv,
              '%': operator.mod
              }
    op = allops[oper]  # get the index value of a dictionary
    return op(op1, op2)


# main program
expr = ['1 + 3', '1 - 3', '1 * 3', '1 % 3']
for x in expr:
    parts = x.split()
    result = eval_binary_expr(*parts)  # * converts list into 3 individual components
    print(x + ': ' + str(result))

ex2 = ' (3 + 2) * 6'  # you can have any arbitrary valid numeric expression
print(eval(ex2))