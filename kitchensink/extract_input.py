#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""


### -------------------- function ----------------------
### extracts and return input & output variable names
### ------------------------------------------------ 
def extract_input_output_names(str):
    
    elm = str.split(";")
    input_var =  elm[0].split('=')[-1]
    ouput_var =  elm[1].split('=')[-1]
    
    return ( input_var.strip() , ouput_var.strip() )

### -------------------- main ----------------------
###
### ------------------------------------------------  

test_data = [  '#@input = a ; @output = b' , 
         '# @input = abc ; @output = bbb' , 
         '# @input = hi ; @output = there' , 
         '# @input = a1_c2 ; @output = b4_c4' ,
         '# @input = a1_c2 ; @output = b4_c4' 
    ]

for x in test_data:
    print (extract_input_output_names(x) )