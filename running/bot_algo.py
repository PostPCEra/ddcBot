#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Om Sri
"""
Created on Fri Feb 23 18:55:45 2018

@author:
"""
import functools
import logging

# ---------- TODO -----------------------------
# 0. Error condition test cases & code changes to handle those
# 1. Logging : https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
# 2. Refactor code
#
# Features :
# DONE : simple arthimatic/geometric sequence
# DONE : Fizz buzz style continuous sequences ( with delta also)
# DONE : categories ( child, teen, adult )
#
# Data structures : Lists, Dictionary, tuple,
#    @input = lst, 3 ; @output = lst2  ( here 3 indicates check for filed 4 ( 0 based) for clue on how to Derive Output
# Date/Time simple input/output conversions
# Filter : student records whose grade below 60%
#  ---------- TODO -----------------------------

# global constants
CAT_TYPE_ALLOTHER = 'allother'  # Category type
REL_TYPE_ARITHMETIC_SEQUENCE = 'arithmetic_sequence'  # Relation type
REL_TYPE_GEOMETRIC_SEQUENCE = 'geometric_sequence'
REL_TYPE_UNKNOWN = 'unknown'

# Global vars, these vars will be Set in main_entry_point() , they will be accessed in generate_code() functions
INPUT_SYMBOL = ''
OUTPUT_SYMBOL = ''

# ------------------- Logging -------------------------
#
# -------------------  *****************  ------------------------
logging.basicConfig(
    filename="log-4-ddcBot.log",
    level=logging.DEBUG,
    format="%(levelname)s:%(message)s"
    # level=logging.INFO,
    # format="%(asctime)s:%(levelname)s:%(message)s"
    )

log = logging.getLogger("ddcB")

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

    log.info(categories)

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

def get_loop_code(varname, value, oper):

    code = "{} = [ ]\n".format(OUTPUT_SYMBOL) + \
           "{} = {} \n".format(varname, value) + \
           "for x in {}:\n\t".format(INPUT_SYMBOL) + \
           "{}.append({} {} x)\n\n".format(OUTPUT_SYMBOL, varname, oper)
    return code

def get_category_code(cat_lst, edge_values):

    code = "{} = [ ]\n".format(OUTPUT_SYMBOL) + \
           "for n in {}:\n\t".format(INPUT_SYMBOL)

    idx = 0
    segment = "if n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(cat_lst[0][0])

    idx = idx + 1
    for key, value in cat_lst[1:]:
        tmp = "elif n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp
        idx = idx + 1

    tmp = "\n{}.append(element)\n\n\t".format(OUTPUT_SYMBOL)

    code = code + segment + tmp
    # print(code)
    return code

def get_sequence_code(dict1, delta):

    from operator import itemgetter

    # convert dictionary to tuple list, then sort. dictonary sorts are hard and unreliable .
    tuple_lst = list(dict1.items())
    print(tuple_lst)
    tuple_lst.sort(key=itemgetter(0))
    tuple_lst.sort(key=itemgetter(1), reverse=True)

    code = "{} = [ ]\n".format(OUTPUT_SYMBOL) + \
           "for n in {}:\n\t".format(INPUT_SYMBOL)

    segment = "if n % {} == 0:\n\t\t".format(tuple_lst[0][1]) + \
                "element = '{}'\n\t".format(tuple_lst[0][0])

    for key, value in tuple_lst[1:]:
        tmp = "elif n % {} == 0:\n\t\t".format(value) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp

    tmp2 = "" if delta == 0 else " + {}".format(delta)
    tmp = "else:\n\t\t" + \
          "element = n {}\n\n".format(tmp2) + \
            "{}.append(element)\n\n\t".format(OUTPUT_SYMBOL)

    code = code + segment + tmp
    print(code)
    return code

def generate_code(categories, cat_relationships):

    length = len(categories)
    log.debug("  num. of Categories in Input data: {}\n:".format(str(length)))

    if length == 1:
        log.debug("  Input data relationship: {}\n:".format(cat_relationships[CAT_TYPE_ALLOTHER]))
        input, output = categories[CAT_TYPE_ALLOTHER]  # input/output values
        if cat_relationships[CAT_TYPE_ALLOTHER] == REL_TYPE_ARITHMETIC_SEQUENCE:
            varname, value, oper = ("delta", output[0]-input[0], "+")
        else:
            varname, value, oper = ("ratio", output[0]/input[0], "*")

        code = get_loop_code(varname, value, oper)
        log.info(code)
        return code

    elif REL_TYPE_UNKNOWN in cat_relationships.values():
        log.debug("********** Unknown relationship in the Input data, let's find out")

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
            log.error("  The Output Categories do not follow Ordered sequence ..\n")
            return " -------- NOT Ordered "

        code = get_category_code(cat_sorted, edge_values)
        log.debug(cat_sorted)
        log.info(code)
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
        log.debug(eachcat_with_onevalue)

        code = get_sequence_code(eachcat_with_onevalue, delta)
        log.info(code)
        return code

# ------------------- process for relationship -------------------------
#
# -------------------  *****************  ---------------------------
def process_for_relationships(input_l, output_l):
    freq_two_or_more = [x for x in output_l if output_l.count(x) > 1]
    output_categories = set(freq_two_or_more)  # removes duplicates

    if len(output_categories) == 0:
        categories = {CAT_TYPE_ALLOTHER: (input_l, output_l)}  # dictionary to hold all distinct category items
    else:
        zip_inout = zip(input_l, output_l)
        categories = extract_categories(zip_inout, output_categories)

    log.debug('\n')
    log.debug(categories)

    cat_relationships = find_all_relationships(categories)

    code = generate_code(categories, cat_relationships)
    #print(code)


def main_entry_point(input_as_symbol, output_as_symbol, in_as_value, out_as_value):
    global INPUT_SYMBOL    # need to state we are accessing Globally declared ones in this local method in order to modify them
    global OUTPUT_SYMBOL
    INPUT_SYMBOL = input_as_symbol  # now access these in code_gen() methods
    OUTPUT_SYMBOL = output_as_symbol

    #input_as_value = eval(input_as_symbol)  # not working for stand alone , so levae it
    input_as_value =  in_as_value
    output_as_value = out_as_value

    log.debug('\n------------- passed input/output values   ----------------')
    log.debug(input_as_symbol)
    log.debug(output_as_symbol)
    log.debug(input_as_value)
    log.debug(output_as_value)

    code = process_for_relationships(input_as_value, output_as_value)   # pass values of variable
    return code
