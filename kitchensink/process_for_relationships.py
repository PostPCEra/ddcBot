#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# global definitions
CAT_TYPE_ALLOTHER = 'allother'  # Category type
REL_TYPE_ARITHMETIC_SEQUENCE = 'arithmetic_sequence'  # Relation type
REL_TYPE_GEOMETRIC_SEQUENCE = 'geometric_sequence'
REL_TYPE_UNKNOWN = 'unknown'


# ------------------- find all relationships -------------------------
#
# -------------------  *****************  ------------------------

def find_relation_input_to_output(input_l, output_l):

    lst = input_l
    lst2 = output_l

    delta = lst2[0] - lst[0]
    in_relation = True
    for ind in range(len(lst)):
        if not (lst2[ind] - lst[ind] == delta):
            in_relation = False
            break

    if in_relation:
        return REL_TYPE_ARITHMETIC_SEQUENCE

    multiple = lst2[1] / lst[0]
    in_relation = True
    for ind in range(len(lst)):
        if not (lst2[ind] / lst[ind] == multiple):
            in_relation = False
            break

    if in_relation:
        return REL_TYPE_GEOMETRIC_SEQUENCE
    else:
        return REL_TYPE_UNKNOWN



def find_relation_among_elements(input_l):

    lst = input_l

    delta = lst[1] - lst[0]
    in_relation = True
    for ind in range(len(lst) - 1):
        if not (lst[ind + 1] - lst[ind] == delta):
            in_relation = False
            break

    if in_relation:
        return REL_TYPE_ARITHMETIC_SEQUENCE

    multiple = lst[1] / lst[0]
    in_relation = True
    for ind in range(len(lst) - 1):
        if not (lst[ind + 1] / lst[ind] == multiple):
            in_relation = False
            break

    if in_relation:
        return REL_TYPE_GEOMETRIC_SEQUENCE
    else:
        return REL_TYPE_UNKNOWN


def find_all_relationships(categories):

    cat_realtionships = {}  # init
    for key, value in categories.items():
        if key == CAT_TYPE_ALLOTHER:
            input_l, output_l = value
            cat_realtionships[key] = find_relation_input_to_output(input_l, output_l)
        else:
            input_l = value
            cat_realtionships[key] = find_relation_among_elements(input_l)

    print(cat_realtionships)
    return cat_realtionships


# ------------------- extract categories -------------------------
#
# -------------------  *****************  ------------------------
def extract_categories(zip_inout, output_categories):

    categories = { CAT_TYPE_ALLOTHER: ([], []) }  # dictionary to hold all distinct category items
    for x in output_categories:
        categories[x] = []

    print(categories)

    zlist = sorted(zip_inout, key=lambda p: p[0])  # sorting  based on the values of x in each (x,y) pair
    for pair in zlist:
        key, value = pair
        if value in categories:
            tmp = categories[value]
            tmp.append(key)
            categories[value] = tmp
        else:
            key_list, value_list = categories[CAT_TYPE_ALLOTHER]
            key_list.append(key)
            value_list.append(value)
            categories[CAT_TYPE_ALLOTHER] = (key_list, value_list)

    return categories


# ------------------- process for relationship -------------------------
#
# -------------------  *****************  ---------------------------
def process_for_relationships(input_l, output_l):

    freq_two_or_more = [x for x in output_l if output_l.count(x) > 1]
    output_categories = set(freq_two_or_more) # removes duplicates
    print(output_categories)

    if len(output_categories) == 0:
        categories = {CAT_TYPE_ALLOTHER: (input_l, output_l)}  # dictionary to hold all distinct category items
    else:
        zip_inout = zip(input_l, output_l)
        categories = extract_categories(zip_inout, output_categories)

    print(categories)

    cat_realtionships = find_all_relationships(categories)


# ------------------- main -------------------------
def main():
    input_l = list(range(1,17))
    output_l = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14 ]
    o = process_for_relationships(input_l, output_l)

# ------------------- call main -------------------
main()

