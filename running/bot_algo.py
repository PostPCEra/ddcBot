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

# Error codes
ERROR_NOT_ARTHIMETIC_GEOMETRIC = "Sorry, I could not find any Arthimatic/Geometric relationship between Input & Output, Pls. check data!!!"

ERROR_LIST = [ ERROR_NOT_ARTHIMETIC_GEOMETRIC, 1
    ]
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

# class to hold category data
class Relationship_data(object):
    input_symbol = ''
    output_symbol = ''
    relationship_type = ''
    value1 = ''
    value2 = 0
    value3 = ''

    def update_symbols(self, input_symbol, output_symbol):
        self.input_symbol = input_symbol
        self.output_symbol = output_symbol

    def update(self, relationship_type, val1, val2=0, val3=''):
        self.relationship_type = relationship_type
        self.value1 = val1
        self.value2 = val2
        self.value3 = val3


REL_OBJ = Relationship_data()  # create new global instance

# ------------------- find all relationships -------------------------------------------
#
# The following group of functions determine the relationship between Input & Ouput Lists
#
# -------------------  *****************  ----------------------------------------------

def find_relation_input_to_output(input, output):

    # no try: catch: required as we are going to pre check to make sure all input/out is either int/float numbers
    global REL_OBJ  # declare global to update obj

    diff = [output[i] - input[i] for i in range(len(input))]
    if len(set(diff)) == 1:   # length will be 1 if all elements are same, because set() returns unique elements
        REL_OBJ.update(REL_TYPE_ARITHMETIC_SEQUENCE, 'delta', diff[0], '+')
        return REL_TYPE_ARITHMETIC_SEQUENCE

    multiple = [output[i] / input[i] for i in range(len(input))]
    if len(set(multiple)) == 1:
        REL_OBJ.update(REL_TYPE_GEOMETRIC_SEQUENCE, 'multiple', multiple[0], '*')
        return REL_TYPE_GEOMETRIC_SEQUENCE

    # if  round() for 3 places same for all elements, then it is integer number
    exponential = [round(math.log10(output[i]) / math.log10(input[i]), 3) for i in range(len(input))]
    log.debug(exponential)
    if len(set(exponential)) == 1:
        if exponential[0] > 1:
            REL_OBJ.update(REL_TYPE_EXPONENTIAL_SEQUENCE, exponential[0])
            return REL_TYPE_EXPONENTIAL_SEQUENCE

        else:
            REL_OBJ.update(REL_TYPE_LOGARITHMIC_SEQUENCE, exponential[0])
            return REL_TYPE_LOGARITHMIC_SEQUENCE

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
            "dt = datetime.datetime.strptime({}, '{}')\n".format(REL_OBJ.input_symbol, formatstr) + \
           "delta = {}  # this is time delta that needs to be added \n".format(delta) + \
           "{} = dt + delta \n".format(REL_OBJ.output_symbol)
    return code

def get_loop_code():
    log.debug('asr fresh******: ' +REL_OBJ.output_symbol)

    code = "{} = [ ]\n".format(REL_OBJ.output_symbol) + \
           "{} = {} \n".format(REL_OBJ.value1, REL_OBJ.value2) + \
           "for x in {}:\n\t".format(REL_OBJ.input_symbol) + \
           "{}.append({} {} x)\n\n".format(REL_OBJ.output_symbol, REL_OBJ.value1, REL_OBJ.value3)

    return code

def get_explog_code():

    code = "{} = [ ]\n".format(REL_OBJ.output_symbol) + \
           "for x in {}:\n\t".format(REL_OBJ.input_symbol) + \
           "{}.append(round(math.pow(x, {})))\n\n".format(REL_OBJ.output_symbol, REL_OBJ.value1)
    return code

def get_category_code(cat_lst, edge_values):

    code = "{} = [ ]\n".format(REL_OBJ.output_symbol) + \
           "for n in {}:\n\t".format(REL_OBJ.input_symbol)

    idx = 0
    segment = "if n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(cat_lst[0][0])

    idx = idx + 1
    for key, value in cat_lst[1:]:
        tmp = "elif n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp
        idx = idx + 1

    tmp = "\n\t{}.append(element)\n\n\t".format(REL_OBJ.output_symbol)

    code = code + segment + tmp
    # print(code)
    return code

def get_sequence_code(dict1, delta):

    from operator import itemgetter

    # convert dictionary to tuple list, then sort. dictonary sorts are hard and unreliable .
    tuple_lst = list(dict1.items())
    tuple_lst.sort(key=itemgetter(0))
    tuple_lst.sort(key=itemgetter(1), reverse=True)

    code = "{} = [ ]\n".format(REL_OBJ.output_symbol) + \
           "for n in {}:\n\t".format(REL_OBJ.input_symbol)

    segment = "if n % {} == 0:\n\t\t".format(tuple_lst[0][1]) + \
                "element = '{}'\n\t".format(tuple_lst[0][0])

    for key, value in tuple_lst[1:]:
        tmp = "elif n % {} == 0:\n\t\t".format(value) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp

    tmp2 = "" if delta == 0 else " + {}".format(delta)
    tmp = "else:\n\t\t" + \
          "element = n {}\n\n\t".format(tmp2) + \
            "{}.append(element)\n\n\t".format(REL_OBJ.output_symbol)

    code = code + segment + tmp
    return code

def generate_code(categories, cat_relationships):

    length = len(categories)
    log.debug("  num. of Categories in Input data: {}\n:".format(str(length)))
    error_state = False

    if length == 1:
        log.debug("  Input data relationship: {}\n:".format(cat_relationships[CAT_TYPE_ALLOTHER]))
        relationship_type = cat_relationships[CAT_TYPE_ALLOTHER]
        log.debug('relationship_type: ' + REL_OBJ.relationship_type)
        log.debug('value1: ' + str(REL_OBJ.value1))
        log.debug('value2: ' + str(REL_OBJ.value2))
        log.debug('value3: ' + str(REL_OBJ.value3))
        if relationship_type in [REL_TYPE_ARITHMETIC_SEQUENCE, REL_TYPE_GEOMETRIC_SEQUENCE]:
            code = get_loop_code()
        elif relationship_type in [REL_TYPE_EXPONENTIAL_SEQUENCE, REL_TYPE_LOGARITHMIC_SEQUENCE]:
            code = get_explog_code()
        else:
            code = ERROR_NOT_ARTHIMETIC_GEOMETRIC

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
    # need to state we are accessing Globally declared ones in this local method in order to modify them
    global REL_OBJ

    # update to global object, so we access these in code_gen() methods
    REL_OBJ.update_symbols(input_as_symbol, output_as_symbol)

    #input_as_value = eval(input_as_symbol)  # not working for stand alone , so levae it
    input_as_value = in_as_value
    output_as_value = out_as_value

    log.debug('\n------------- passed input/output values   ----------------')
    log.debug(input_as_symbol)
    log.debug(output_as_symbol)
    log.debug(input_as_value)
    log.debug(output_as_value)

    code = process_for_relationships(input_as_value, output_as_value)   # pass values of variable
    return code
