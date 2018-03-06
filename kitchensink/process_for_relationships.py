#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# global constants
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

    multiple = lst2[0] / lst[0]
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

# ------------------- generate CODE  -------------------------
#

def get_loop_code(varname, value, oper,input_symbol, output_symbol):

    code = "{} = [ ]\n".format(output_symbol) + \
           "{} = {} \n".format(varname, value) + \
           "for x in {}:\n\t".format(input_symbol) + \
           "{}.append({} {} x)\n\n\t".format(output_symbol, varname, oper)
    return code

def generate_code(categories, cat_relationships):

    length = len(categories)
    if length == 1:
        input, output = categories[CAT_TYPE_ALLOTHER]  # input/output values
        if cat_relationships[CAT_TYPE_ALLOTHER] == REL_TYPE_ARITHMETIC_SEQUENCE:
            varname, value, oper = ("delta", output[0]-input[0], "+")
        else:
            varname, value, oper = ("ratio", output[0]/input[0], "*")

        input_symbol, output_symbol = 'a', 'b'
        code = get_loop_code(varname, value, oper, input_symbol, output_symbol)
        #print(code)
        return code

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

    cat_relationships = find_all_relationships(categories)

    code = generate_code(categories, cat_relationships)
    print(code)


# ------------------- main -------------------------
#
# ---------------------------------------------------

def main():

    test_suite = [  ([1, 5, 8], [6, 10, 13]),
                    ([2, 6, 7], [10, 30, 35]),
                    (list(range(1, 15)), [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14] )
                 ]

    for pair in test_suite:
        input, output = pair
        o = process_for_relationships(input, output)

# ------------------- call main -------------------
main()

