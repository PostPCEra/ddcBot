#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Om Sri
"""
Created on Fri Feb 23 18:55:45 2018

@author:
"""
import functools
import datetime
import math

# ------------------- application specific imports
import global_const as gc
import generate_code as gencode
import validate_if_numericio as validate_numeric

# ---------- TODO -----------------------------
# 0. Error condition test cases & code changes to handle those
# DONE : 1. Logging : https://www.digitalocean.com/community/tutorials/how-to-use-gc.logging-in-python-3
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



# ------------------- find all relationships -------------------------------------------
#
# The following group of functions determine the relationship between Input & Ouput Lists
#
# -------------------  *****************  ----------------------------------------------

def find_relation_input_to_output(input, output):

    # no try: catch: required as we are going to pre check to make sure all input/out is either int/float numbers
    #global gc.REL_OBJ  # declare global to update obj

    diff = [output[i] - input[i] for i in range(len(input))]
    if len(set(diff)) == 1:   # length will be 1 if all elements are same, because set() returns unique elements
        gc.REL_OBJ.update(gc.REL_TYPE_ARITHMETIC_SEQUENCE, 'delta', diff[0], '+')
        return gc.REL_TYPE_ARITHMETIC_SEQUENCE

    multiple = [output[i] / input[i] for i in range(len(input))]
    if len(set(multiple)) == 1:
        gc.REL_OBJ.update(gc.REL_TYPE_GEOMETRIC_SEQUENCE, 'multiple', multiple[0], '*')
        return gc.REL_TYPE_GEOMETRIC_SEQUENCE

    # if  round() for 3 places same for all elements, then it is integer number
    exponential = [round(math.log10(output[i]) / math.log10(input[i]), 3) for i in range(len(input))]
    gc.log.debug(exponential)
    if len(set(exponential)) == 1:
        if exponential[0] > 1:
            gc.REL_OBJ.update(gc.REL_TYPE_EXPONENTIAL_SEQUENCE, exponential[0])
            return gc.REL_TYPE_EXPONENTIAL_SEQUENCE

        else:
            gc.REL_OBJ.update(gc.REL_TYPE_LOGARITHMIC_SEQUENCE, exponential[0])
            return gc.REL_TYPE_LOGARITHMIC_SEQUENCE

    # if not any one of above
    return gc.REL_TYPE_UNKNOWN

# ------------------- find_relation_among_elements -------------------------
def find_relation_among_elements(input):

    diff = [input[i+1] - input[i] for i in range(len(input) - 1)]
    if len(set(diff)) == 1:
        return gc.REL_TYPE_ARITHMETIC_SEQUENCE

    multiple = [input[i+1] / input[i] for i in range(len(input) - 1)]
    if len(set(multiple)) == 1:
        return gc.REL_TYPE_GEOMETRIC_SEQUENCE

    # if not any one of above
    return gc.REL_TYPE_UNKNOWN

# ------------------- find_all_relationships -------------------------
def find_all_relationships(categories):

    cat_realtionships = {}  # init
    for key, value in categories.items():
        if key == gc.CAT_TYPE_ALLOTHER:
            input_l, output_l = value
            cat_realtionships[key] = find_relation_input_to_output(input_l, output_l)
        else:
            input_l = value
            cat_realtionships[key] = find_relation_among_elements(input_l)

    gc.log.debug(cat_realtionships)
    return cat_realtionships


# ------------------- extract categories -------------------------
#
# -------------------  *****************  ------------------------
def extract_categories(zip_inout, output_categories):

    categories = { gc.CAT_TYPE_ALLOTHER: ([], []) }  # dictionary to hold all distinct category items
    for x in output_categories:
        categories[x] = []

    gc.log.info(categories)

    zlist = sorted(zip_inout, key=lambda p: p[0])  # sorting  based on the values of x in each (x,y) pair
    for pair in zlist:
        key, value = pair
        if value in categories:
            tmp = categories[value]
            tmp.append(key)
            categories[value] = tmp
        else:
            key_list, value_list = categories[gc.CAT_TYPE_ALLOTHER]
            key_list.append(key)
            value_list.append(value)
            categories[gc.CAT_TYPE_ALLOTHER] = (key_list, value_list)

    lst1, lst2 = categories[gc.CAT_TYPE_ALLOTHER]
    if len(lst1) == 0:
        categories.pop(gc.CAT_TYPE_ALLOTHER, None)  # since lists are empty remove key

    return categories



def parse_relationships_and_invoke_generate_code(categories, cat_relationships):

    length = len(categories)
    gc.log.debug("  num. of Categories in Input data: {}\n:".format(str(length)))
    error_state = False

    if length == 1:
        gc.log.debug("  Input data relationship: {}\n:".format(cat_relationships[gc.CAT_TYPE_ALLOTHER]))
        relationship_type = cat_relationships[gc.CAT_TYPE_ALLOTHER]
        gc.log.debug('relationship_type: ' + gc.REL_OBJ.relationship_type)
        gc.log.debug('value1: ' + str(gc.REL_OBJ.value1))
        gc.log.debug('value2: ' + str(gc.REL_OBJ.value2))
        gc.log.debug('value3: ' + str(gc.REL_OBJ.value3))
        if relationship_type in [gc.REL_TYPE_ARITHMETIC_SEQUENCE, gc.REL_TYPE_GEOMETRIC_SEQUENCE]:
            code = gencode.get_loop_code()
        elif relationship_type in [gc.REL_TYPE_EXPONENTIAL_SEQUENCE, gc.REL_TYPE_LOGARITHMIC_SEQUENCE]:
            code = gencode.get_explog_code()
        else:
            code = gc.ERROR_NOT_ARTHIMETIC_GEOMETRIC

        return code

    elif gc.REL_TYPE_UNKNOWN in cat_relationships.values():
        gc.log.debug("********** Unknown relationship in the Input data, let's find out")

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

        gc.log.info(edge_values)

        if not ordered_category:
            gc.log.error("  The Output Categories do not follow Ordered sequence ..\n")
            return " -------- NOT Ordered "

        gc.log.debug(cat_sorted)
        code = gencode.get_category_code(cat_sorted, edge_values)  # category is Fizz Buzz
        return code

    else:
        eachcat_with_onevalue = {}  # init
        for key, value in categories.items():
            if key == gc.CAT_TYPE_ALLOTHER:
                input_l, output_l = value
                delta = output_l[0] - input_l[0]
                eachcat_with_onevalue[key] = delta
            else:
                eachcat_with_onevalue[key] = value[0]


        delta = eachcat_with_onevalue.pop(gc.CAT_TYPE_ALLOTHER, None) # save value and remove key
        gc.log.debug(eachcat_with_onevalue)

        code = gencode.get_sequence_code(eachcat_with_onevalue, delta) # sequence  'child', 'teen' based on age
        return code


def process_for_objects(input, output):
    field_name = gc.REL_OBJ.input2_symbol
    #code = gencode.gen_objects_code()
    #return code
    return 'code 2222'

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
    code = gencode.gen_dates_code(delta,formatstr)
    return code

# ------------------- process for relationship -------------------------
#
# -------------------  *****************  ---------------------------

def process_for_relationships(input_l, output_l):

    if isinstance(input_l, list):
        field_name = gc.REL_OBJ.input2_symbol
        try:
            gc.log.debug('input_l[0].' + field_name + '----')
            gc.log.debug(input_l[0].name)
            gc.log.debug(input_l[0].age)
            val = eval('input_l[0].' + field_name)
            gc.log.debug('value of the field is:' + val)
            code = gencode.gen_objects_code()
            #code2 = process_for_objects(input_l, output_l)
            #return 'code'
            return code

        except Exception as e:
            gc.log.debug('it is not class object, so proceed further')
            pass



    if isinstance(input_l, str):
        code = process_for_dates(input_l, output_l)
        return code

    msg = validate_numeric.validate_if_numeric_inputoutput(input_l, output_l)
    if msg != "continue":
        return msg

    input_types = [str(type(x)) for x in input_l]
    if "<class 'str'>" in input_types:
        return "Sorry, I can not handle Input LISTS with Strings  at this time !!!!!!!"

    freq_two_or_more = [x for x in output_l if output_l.count(x) > 1]
    output_categories = set(freq_two_or_more)  # removes duplicates

    if len(output_categories) == 0:
        categories = {gc.CAT_TYPE_ALLOTHER: (input_l, output_l)}  # dictionary to hold all distinct category items
    else:
        zip_inout = zip(input_l, output_l)
        categories = extract_categories(zip_inout, output_categories)

    gc.log.debug('\n')
    gc.log.debug(categories)

    cat_relationships = find_all_relationships(categories)

    code = parse_relationships_and_invoke_generate_code(categories, cat_relationships)
    gc.log.info(code)
    return code


def main_entry_point(input_as_symbol, output_as_symbol, in_as_value, out_as_value, input2_as_symbol):
    # need to state we are accessing Globally declared ones in this local method in order to modify them
    #global gc.REL_OBJ

    # update to global object, so we access these in code_gen() methods
    gc.REL_OBJ.update_symbols(input_as_symbol, output_as_symbol, input2_as_symbol)

    #input_as_value = eval(input_as_symbol)  # not working for stand alone , so levae it
    input_as_value = in_as_value
    output_as_value = out_as_value

    gc.log.debug('\n------------- passed input/output values   ----------------')
    gc.log.debug(input_as_symbol)
    gc.log.debug(output_as_symbol)
    gc.log.debug(input2_as_symbol)
    gc.log.debug(input_as_value)
    gc.log.debug(output_as_value)

    code = process_for_relationships(input_as_value, output_as_value)   # pass values of variable
    return code
