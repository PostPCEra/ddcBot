#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""


# -------------------- function ----------------------
# extracts and return input & output variable names
# ------------------------------------------------
def extract_input_output_names(string):
    elm = string.split(";")
    input_var = elm[0].split('=')[-1]
    output_var = elm[1].split('=')[-1]

    return input_var.strip(), output_var.strip()


# ----------------------- main ----------------------
#
# ------------------------------------------------

test_data = ['#@input = a ; @output = b',
             '# @input = abc ; @output = bbb',
             '# @input = hi ; @output = there',
             '# @input = a1_c2 ; @output = b4_c4',
             '# @input = a ; @output = b'
             ]

for x in test_data:
    print(extract_input_output_names(x))

# now do with a complete input & output variables
a = [ 1, 3, 5]
b = [ 2, 6, 10]
iostr = '# @input = a ; @output = b'
instr, outstr = extract_input_output_names(iostr)
invar, outvar =  eval(instr), eval(outstr)

factor = outvar[0] / invar[0]
b = [ factor * x for x in a]
print(b)




