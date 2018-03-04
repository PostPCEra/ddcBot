#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# ------------------- extract relationship -------------------------
#
# -------------------  *****************  ---------------------------
def extract_relationship(inp, outp):

    zp = zip(inp, outp)
    zlist = sorted(zp, key=lambda p: p[0])  # sorting  based on the values of x in each (x,y) pair

    two_or_more = [x for x in outp if outp.count(x) > 1]
    category_list = set(two_or_more) # removes duplicates
    print(category_list)

    occr = { 'remaining' : ([ ], [ ]) }
    for x in category_list:
        occr[x] = [ ]

    print(occr)

    for pair in zlist:
        key, value = pair
        if value in category_list:
            tmp = occr[value]
            tmp.append(key)
            occr[value] = tmp
        else:
            key_list, value_list = occr['remaining']
            key_list.append(key)
            value_list.append(value)
            occr['remaining'] = (key_list, value_list)

    print(occr)

    in_l, out_l = occr['remaining']
    diff = in_l[0] - out_l[0]
    for i, _ in enumerate(in_l):
        if ( (in_l[i] - out_l[i]) != diff ):
            print(False)



# ------------------- main -------------------------
def main():
    input_l = list(range(1,17))
    output_l = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14 ]
    o = extract_relationship(input_l, output_l)

# ------------------- call main -------------------
main()

from fractions import gcd
lis = [3, 6, 9, 12]
result = gcd(*lis[:2])  #get the gcd of first two numbers
if len(lis) >2:
    for x in lis[2:]:    #now iterate over the list starting from the 3rd element
        result = gcd(result,x)
print(result)
