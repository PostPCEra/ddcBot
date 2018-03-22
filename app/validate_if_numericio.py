
import global_const as gc
import generate_code as gencode

def validate_if_numeric_inputoutput(input, output):

    cls_int, cls_float, cls_str = "<class 'int'>", "<class 'float'>", "<class 'str'>"
    in_type, out_type = str(type(input)), str(type(output))

    if in_type in [cls_int, cls_float]:
        if out_type in [cls_int, cls_float]:
            return handle_one_to_one()
        else:
            error = "Sorry, When Input type is int/float output should be similar type !!"
            return error
    elif in_type == cls_str:
        error = "Sorry, I do not support  String data as INPUT at this time!!"
        return error

    in_types = [str(type(x)) for x in input]
    in_set = "".join(set(in_types))  # join as one single string so easy to compare below

    possibilities = [cls_int, cls_float, cls_float + cls_int, cls_int + cls_float]
    error = ''
    if cls_str in in_types:
        error = "Sorry, I do not support String data as part of  INPUT List at this time!!"
        return error

    # this is to test if any 'List of Lists' or 'tuples' exists in iNPUT
    if in_set not in possibilities:
        error = "Sorry, I do not support 'nested LISTS' as part of  INPUT List at this time!!!"
        return error

    # at this point in flow INPUT  is valid LIST, if OUTPUT is single value, call the handle function,
    if out_type in [cls_int, cls_float]:
        return handle_list_to_one(input, output)
    else:
        #error = "call other routines, it may be fizz buzz like INPUT number list, output mix list"
        error = "continue"
        return error


def handle_one_to_one():
    return 'one to one : int or float'


def handle_list_to_one(input, output):
    code = 'no code generated'
    init_value = "{}[0]".format(gc.REL_OBJ.input_symbol)
    if sum(input) == output:
        gc.REL_OBJ.update(gc.REL_TYPE_LIST_TO_ONE_SUM, 'sum', 0, '+')
    elif max(input) == output:
        gc.REL_OBJ.update(gc.REL_TYPE_LIST_TO_ONE_MAX, 'max', init_value, '>')
    elif min(input) == output:
        gc.REL_OBJ.update(gc.REL_TYPE_LIST_TO_ONE_MIN, 'min', init_value, '<')
    elif sum(input)/len(input) == output:
        gc.REL_OBJ.update(gc.REL_TYPE_LIST_TO_ONE_MEAN, 'sum', 0, '+')

    if gc.REL_OBJ.relationship_type in [gc.REL_TYPE_LIST_TO_ONE_SUM, gc.REL_TYPE_LIST_TO_ONE_MAX, gc.REL_TYPE_LIST_TO_ONE_MIN, gc.REL_TYPE_LIST_TO_ONE_MEAN]:
        code = gencode.gen_list_to_one_code()

    return code


