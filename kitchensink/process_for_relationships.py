#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
import functools

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

    lst1, lst2 = categories[CAT_TYPE_ALLOTHER]
    if len(lst1) == 0:
        categories.pop(CAT_TYPE_ALLOTHER, None)  # since lists are empty remove key

    return categories

# ------------------- generate CODE  -------------------------
#

def get_loop_code(varname, value, oper,input_symbol, output_symbol):

    code = "{} = [ ]\n".format(output_symbol) + \
           "{} = {} \n".format(varname, value) + \
           "for x in {}:\n\t".format(input_symbol) + \
           "{}.append({} {} x)\n\n".format(output_symbol, varname, oper)
    return code

def get_category_code(cat_lst, edge_values, input_symbol, output_symbol):

    code = "{} = [ ]\n".format(output_symbol) + \
           "for n in {}:\n\t".format(input_symbol)

    idx = 0
    segment = "if n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(cat_lst[0][0])

    idx = idx + 1
    for key, value in cat_lst[1:]:
        tmp = "elif n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp
        idx = idx + 1

    tmp = "\n{}.append(element)\n\n\t".format(output_symbol)

    code = code + segment + tmp
    # print(code)
    return code

def get_sequence_code(dict1, delta,  input_symbol, output_symbol):

    from operator import itemgetter

    # convert dictionary to tuple list, then sort. dictonary sorts are hard and unreliable .
    tuple_lst = list(dict1.items())
    print(tuple_lst)
    tuple_lst.sort(key=itemgetter(0))
    tuple_lst.sort(key=itemgetter(1), reverse=True)

    code = "{} = [ ]\n".format(output_symbol) + \
           "for n in {}:\n\t".format(input_symbol)

    segment = "if n % {} == 0:\n\t\t".format(tuple_lst[0][1]) + \
                "element = '{}'\n\t".format(tuple_lst[0][0])

    for key, value in tuple_lst[1:]:
        tmp = "elif n % {} == 0:\n\t\t".format(value) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp

    tmp2 = "" if delta == 0 else " + {}".format(delta)
    tmp = "else:\n\t\t" + \
          "element = n {}\n\n".format(tmp2) + \
            "{}.append(element)\n\n\t".format(output_symbol)

    code = code + segment + tmp
    print(code)
    return code

def generate_code(categories, cat_relationships):

    input_symbol, output_symbol = 'a', 'b'

    length = len(categories)
    if length == 1:
        input, output = categories[CAT_TYPE_ALLOTHER]  # input/output values
        if cat_relationships[CAT_TYPE_ALLOTHER] == REL_TYPE_ARITHMETIC_SEQUENCE:
            varname, value, oper = ("delta", output[0]-input[0], "+")
        else:
            varname, value, oper = ("ratio", output[0]/input[0], "*")

        code = get_loop_code(varname, value, oper, input_symbol, output_symbol)
        #print(code)
        return code

    elif REL_TYPE_UNKNOWN in cat_relationships.values():
        print('********** Unknown relationship')

        cat_lst = list(categories.items())
        #print(cat_lst)
        def docompare(item1, item2):
            val1, val2 = item1[1], item2[1]
            return val1[0] - val2[0]

        cat_sorted = sorted(cat_lst, key=functools.cmp_to_key(docompare))
        print(cat_sorted)

        first_item = cat_sorted[0][1]
        small = first_item[0]
        edge_values = [first_item[-1]]
        ordered_category = True

        for _, item in cat_sorted[1:]:
            if small < item[0]:
                small = item[0]
                edge_values.append(item[-1])
            else:
                ordered_category = False
                break

        print(edge_values)

        if not ordered_category:
            return " -------- NOT Ordered "

        code = get_category_code(cat_sorted, edge_values, input_symbol, output_symbol)
        return code

    else:
        eachcat_with_onevalue = {}  # init
        for key, value in categories.items():
            if key == CAT_TYPE_ALLOTHER:
                input_l, output_l = value
                delta = output_l[0] - input_l[0]
                eachcat_with_onevalue[key] = delta
            else:
                eachcat_with_onevalue[key] = value[0]


        delta = eachcat_with_onevalue.pop(CAT_TYPE_ALLOTHER, None) # save value and remove key
        print(eachcat_with_onevalue)

        code = get_sequence_code(eachcat_with_onevalue, delta,  input_symbol, output_symbol)
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
                    (list(range(1, 15)), [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14] ),
                    ([2, 6,12, 13,15, 19, 20, 58], ['child', 'child', 'child', 'teen', 'teen', 'teen', 'adult', 'adult'])
                 ]

    for pair in test_suite:
        input, output = pair
        o = process_for_relationships(input, output)

# ------------------- call main -------------------
# invoke/call main() only when this stand alone file is executed as '$python <file.py>'
# when this file is imported into another file, main() is NOT called
if __name__ == '__main__':
    main()

