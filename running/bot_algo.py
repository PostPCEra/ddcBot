#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Om Sri
"""
Created on Fri Feb 23 18:55:45 2018

@author:
"""
import functools
import logging
import datetime
import math

# ---------- TODO -----------------------------
# 0. Error condition test cases & code changes to handle those
# DONE : 1. Logging : https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
# 2. Refactor code
#
# Features :
# DONE : simple arthimatic/geometric sequence
# DONE : Fizz buzz style continuous sequences ( with delta also)
# DONE : categories ( child, teen, adult )
#
# Data structures : Lists, Dictionary, tuple,
#    @input = lst, 3 ; @output = lst2  ( here 3 indicates check for filed 4 ( 0 based) for clue on how to Derive Output
# https://stackoverflow.com/questions/35490420/how-to-check-type-of-object-in-python
# Date/Time simple input/output conversions
#    https://pymotw.com/2/datetime/
# Filter : student records whose grade below 60%
#  ---------- TODO -----------------------------

# global constants
CAT_TYPE_ALLOTHER = 'allother'  # Category type
REL_TYPE_ARITHMETIC_SEQUENCE = 'arithmetic_sequence'  # Relation type
REL_TYPE_GEOMETRIC_SEQUENCE = 'geometric_sequence'
REL_TYPE_EXPONENTIAL_SEQUENCE = 'exponential_sequence'
REL_TYPE_LOGARITHMIC_SEQUENCE = 'logarithmic_sequence'
REL_TYPE_UNKNOWN = 'unknown'
PASS_VALUE1 = ''

# Error codes
ERROR_NOT_ARTHIMETIC_GEOMETRIC = "Sorry, I could not find any Arthimatic/Geometric relationship between Input & Output, Pls. check data!!!"
ERROR_LIST = [ ERROR_NOT_ARTHIMETIC_GEOMETRIC,

    1
]

# Global vars, these vars will be Set in main_entry_point() , they will be accessed in generate_code() functions
INPUT_SYMBOL = ''
OUTPUT_SYMBOL = ''

# ------------------- Logging -------------------------
#
# -------------------  *****************  ------------------------

# https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings
def setup_logger(filename="/Users/padma/ddcBot/log/log-4-ddcBot.log"):

    logging.basicConfig(
        filename=filename,
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s"
        # level=logging.INFO,
        # format="%(asctime)s:%(levelname)s:%(message)s"
        )

    logger = logging.getLogger("ddcB")
    return logger

# Logging Tutorial : https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
log = setup_logger()

# ------------------- find all relationships -------------------------------------------
#
# The following group of functions determine the relationship between Input & Ouput Lists
#
# -------------------  *****************  ----------------------------------------------

def find_relation_input_to_output(input, output):

    # no try: catch: required as we are going to pre check to make sure all input/out is either int/float numbers

    diff = [output[i] - input[i] for i in range(len(input))]
    if len(set(diff)) == 1:   # length will be 1 if all elements are same, because set() returns unique elements
        return REL_TYPE_ARITHMETIC_SEQUENCE
        # return REL_TYPE_ARITHMETIC_SEQUENCE, diff[0]

    multiple = [output[i] / input[i] for i in range(len(input))]
    if len(set(multiple)) == 1:
        return REL_TYPE_GEOMETRIC_SEQUENCE
        # return REL_TYPE_GEOMETRIC_SEQUENCE, multiple[0]

    exponential = [round(math.log10(output[i]) / math.log10(input[i]), 3) for i in range(len(input))]
    log.debug(exponential)
    log.debug(exponential[0])
    if len(set(exponential)) == 1:
        global PASS_VALUE1
        PASS_VALUE1 = exponential[0]   # set to global value
        log.debug(PASS_VALUE1)
        if exponential[0] > 1:
            return REL_TYPE_EXPONENTIAL_SEQUENCE
            # if above round() for 2 places same for all elements, then it is integer number
            # return REL_TYPE_GEOMETRIC_SEQUENCE, round(exponential[0])

        else:
            return REL_TYPE_LOGARITHMIC_SEQUENCE
            # math.pow(32, 1/5)


    # if not any one of above
    return REL_TYPE_UNKNOWN

# ------------------- find_relation_among_elements -------------------------
def find_relation_among_elements(input):

    diff = [input[i+1] - input[i] for i in range(len(input) - 1)]
    if len(set(diff)) == 1:
        return REL_TYPE_ARITHMETIC_SEQUENCE

    multiple = [input[i+1] / input[i] for i in range(len(input) - 1)]
    if len(set(multiple)) == 1:
        return REL_TYPE_GEOMETRIC_SEQUENCE

    # if not any one of above
    return REL_TYPE_UNKNOWN

# ------------------- find_all_relationships -------------------------
def find_all_relationships(categories):

    cat_realtionships = {}  # init
    for key, value in categories.items():
        if key == CAT_TYPE_ALLOTHER:
            input_l, output_l = value
            cat_realtionships[key] = find_relation_input_to_output(input_l, output_l)
        else:
            input_l = value
            cat_realtionships[key] = find_relation_among_elements(input_l)

    log.debug(cat_realtionships)
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

def gen_dates_code(delta, formatstr):
    code = "import datetime\n" + \
            "dt = datetime.datetime.strptime({}, '{}')\n".format(INPUT_SYMBOL, formatstr) + \
           "delta = {}  # this is time delta that needs to be added \n".format(delta) + \
           "{} = dt + delta \n".format(OUTPUT_SYMBOL)
    return code

def get_loop_code(varname, value, oper):

    code = "{} = [ ]\n".format(OUTPUT_SYMBOL) + \
           "{} = {} \n".format(varname, value) + \
           "for x in {}:\n\t".format(INPUT_SYMBOL) + \
           "{}.append({} {} x)\n\n".format(OUTPUT_SYMBOL, varname, oper)
    return code

def get_explog_code(relationship_type):

    code = "{} = [ ]\n".format(OUTPUT_SYMBOL) + \
           "for x in {}:\n\t".format(INPUT_SYMBOL) + \
           "{}.append(round(math.pow(x, {})))\n\n".format(OUTPUT_SYMBOL, PASS_VALUE1)
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

    tmp = "\n\t{}.append(element)\n\n\t".format(OUTPUT_SYMBOL)

    code = code + segment + tmp
    # print(code)
    return code

def get_sequence_code(dict1, delta):

    from operator import itemgetter

    # convert dictionary to tuple list, then sort. dictonary sorts are hard and unreliable .
    tuple_lst = list(dict1.items())
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
          "element = n {}\n\n\t".format(tmp2) + \
            "{}.append(element)\n\n\t".format(OUTPUT_SYMBOL)

    code = code + segment + tmp
    return code

def generate_code(categories, cat_relationships):

    length = len(categories)
    log.debug("  num. of Categories in Input data: {}\n:".format(str(length)))
    error_state = False

    if length == 1:
        log.debug("  Input data relationship: {}\n:".format(cat_relationships[CAT_TYPE_ALLOTHER]))
        input, output = categories[CAT_TYPE_ALLOTHER]  # input/output values

        relationship_type  = cat_relationships[CAT_TYPE_ALLOTHER]
        if relationship_type == REL_TYPE_ARITHMETIC_SEQUENCE:
            varname, value, oper = ("delta", output[0]-input[0], "+")

        elif relationship_type == REL_TYPE_GEOMETRIC_SEQUENCE:
            ratio = output[0]/input[0]
            if int(ratio) == ratio:
                ratio = int(ratio)
            varname, value, oper = ("ratio", ratio, "*")
        elif relationship_type == REL_TYPE_EXPONENTIAL_SEQUENCE:
            pass
        elif relationship_type == REL_TYPE_LOGARITHMIC_SEQUENCE:
            pass
        else:
            error_state = True

        if error_state:
            code = ERROR_NOT_ARTHIMETIC_GEOMETRIC
        elif relationship_type in [ REL_TYPE_EXPONENTIAL_SEQUENCE, REL_TYPE_LOGARITHMIC_SEQUENCE]:
            code = get_explog_code(relationship_type)
        else:
            code = get_loop_code(varname, value, oper)

        return code

    elif REL_TYPE_UNKNOWN in cat_relationships.values():
        log.debug("********** Unknown relationship in the Input data, let's find out")

        cat_lst = list(categories.items())
        #print(cat_lst)
        def docompare(item1, item2):
            val1, val2 = item1[1], item2[1]
            return val1[0] - val2[0]

        cat_sorted = sorted(cat_lst, key=functools.cmp_to_key(docompare))

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

        log.info(edge_values)

        if not ordered_category:
            log.error("  The Output Categories do not follow Ordered sequence ..\n")
            return " -------- NOT Ordered "

        log.debug(cat_sorted)
        code = get_category_code(cat_sorted, edge_values)  # category is Fizz Buzz
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

        code = get_sequence_code(eachcat_with_onevalue, delta) # sequence  'child', 'teen' based on age
        return code


def process_for_dates(dtstr1, dtstr2):

    formatstr = ''
    def string_to_dt(dtstr):
        format1, format2 = "%Y-%m-%d", "%m-%d-%Y"
        try:
            dt = datetime.datetime.strptime(dtstr, format1)  # if exception , try format2
            formatstr = format1
        except ValueError:
            dt = datetime.datetime.strptime(dtstr, format2)
            formatstr = format2

        return dt, formatstr

    d2, formatstr = string_to_dt(dtstr2)
    d1, _      = string_to_dt(dtstr1)
    delta = d2 - d1
    code = gen_dates_code(delta,formatstr)
    return code

# ------------------- process for relationship -------------------------
#
# -------------------  *****************  ---------------------------
def process_for_relationships(input_l, output_l):

    if isinstance(input_l, str):
        code = process_for_dates(input_l, output_l)
        return code

    input_types = [str(type(x)) for x in input_l]
    if "<class 'str'>" in input_types:
        return "Sorry, I can not handle Input LISTS with Strings  at this time !!!!!!!"

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
    log.info(code)
    return code


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
