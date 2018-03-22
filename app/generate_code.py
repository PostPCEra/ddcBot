
import global_const as gc

# ------------------- generate CODE  -------------------------
#

def gen_dates_code(delta, formatstr):
    #code = "import datetime\n" + \
    code = "dt = datetime.datetime.strptime({}, '{}')\n".format(gc.REL_OBJ.input_symbol, formatstr) + \
           "delta = {}  # this is time delta that needs to be added \n".format(delta.days) + \
           "dt = dt + datetime.timedelta(days=delta) \n" + \
           "{} = datetime.datetime.strftime(dt, '{}')\n".format(gc.REL_OBJ.output_symbol, formatstr)

    return code

def gen_list_to_one_code():
    code = "{} = {}     # initialize variable \n".format(gc.REL_OBJ.value1, gc.REL_OBJ.value2) + \
           "for x in {}:\n\t".format(gc.REL_OBJ.input_symbol)

    if gc.REL_OBJ.relationship_type in [gc.REL_TYPE_LIST_TO_ONE_MAX, gc.REL_TYPE_LIST_TO_ONE_MIN]:
        code = code + "if x {} {}: \n\t\t{} = x\n\n".format(gc.REL_OBJ.value3, gc.REL_OBJ.value1, gc.REL_OBJ.value1)
    else:
        code = code + "{} = {} {} x\n\n".format(gc.REL_OBJ.value1, gc.REL_OBJ.value1, gc.REL_OBJ.value3)

    value1mod = gc.REL_OBJ.value1
    if gc.REL_OBJ.relationship_type == gc.REL_TYPE_LIST_TO_ONE_MEAN:
        code = code + "mean = {} / len({}):\n".format(gc.REL_OBJ.value1, gc.REL_OBJ.input_symbol)
        value1mod = "mean"

    code = code +"{} = {}     # assign final value to output variable \n".format(gc.REL_OBJ.output_symbol, value1mod) + \
           "print({})\n".format(gc.REL_OBJ.output_symbol)
    return code


def get_loop_code():
    code = "{} = [ ]\n".format(gc.REL_OBJ.output_symbol) + \
           "{} = {} \n".format(gc.REL_OBJ.value1, gc.REL_OBJ.value2) + \
           "for x in {}:\n\t".format(gc.REL_OBJ.input_symbol) + \
           "{}.append({} {} x)\n\n".format(gc.REL_OBJ.output_symbol, gc.REL_OBJ.value1, gc.REL_OBJ.value3)
    return code


def get_explog_code():

    code = "{} = [ ]\n".format(gc.REL_OBJ.output_symbol) + \
           "for x in {}:\n\t".format(gc.REL_OBJ.input_symbol) + \
           "{}.append(round(math.pow(x, {})))\n\n".format(gc.REL_OBJ.output_symbol, gc.REL_OBJ.value1)
    return code

def get_category_code(cat_lst, edge_values):

    code = "{} = [ ]\n".format(gc.REL_OBJ.output_symbol) + \
           "for n in {}:\n\t".format(gc.REL_OBJ.input_symbol)

    idx = 0
    segment = "if n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(cat_lst[0][0])

    idx = idx + 1
    for key, value in cat_lst[1:]:
        tmp = "elif n <= {}:\n\t\t".format(edge_values[idx]) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp
        idx = idx + 1

    tmp = "\n\t{}.append(element)\n\n\t".format(gc.REL_OBJ.output_symbol)

    code = code + segment + tmp
    # print(code)
    return code

def get_sequence_code(dict1, delta):

    from operator import itemgetter

    # convert dictionary to tuple list, then sort. dictonary sorts are hard and unreliable .
    tuple_lst = list(dict1.items())
    tuple_lst.sort(key=itemgetter(0))
    tuple_lst.sort(key=itemgetter(1), reverse=True)

    code = "{} = [ ]\n".format(gc.REL_OBJ.output_symbol) + \
           "for n in {}:\n\t".format(gc.REL_OBJ.input_symbol)

    segment = "if n % {} == 0:\n\t\t".format(tuple_lst[0][1]) + \
                "element = '{}'\n\t".format(tuple_lst[0][0])

    for key, value in tuple_lst[1:]:
        tmp = "elif n % {} == 0:\n\t\t".format(value) + \
                "element = '{}'\n\t".format(key)
        segment = segment + tmp

    tmp2 = "" if delta == 0 else " + {}".format(delta)
    tmp = "else:\n\t\t" + \
          "element = n {}\n\n\t".format(tmp2) + \
            "{}.append(element)\n\n\t".format(gc.REL_OBJ.output_symbol)

    code = code + segment + tmp
    return code
