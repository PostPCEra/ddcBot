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

# ------------------- extract relationship -------------------------
#
# -------------------  *****************  ---------------------------
def extract_relationship(inp, outp):

    zp = zip(inp, outp)
    zlist = sorted(zp, key=lambda p: p[0])  # sorting  based on the values of x in each (x,y) pair

    two_or_more = [x for x in outp if outp.count(x) > 1]
    category_list = set(two_or_more) # removes duplicates
    print(category_list)
    # https: // stackoverflow.com / questions / 473099 / check - if -a - given - key - already - exists - in -a - dictionary - and -increment - it
    occr = { 'remaining' : [ ] }
    for x in uniq:
        occr[x] = [ ]

    a = occr['remaining']
    print(occr)

    for pair in zlist:
        key, value = pair
        if value in category_list:
            tmp = occr[value]
            tmp.append(key)
            occr[value] = tmp
        else:
            tmp = occr['remaining']
            tmp.append(key)
            occr['remaining'] = tmp

    print(occr)
# ------------------- main -------------------------
def main():
    input_l = list(range(1,17))
    output_l = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14 ]
    o = extract_relationship(input_l, output_l)

# ------------------- call main -------------------
main()

