
def handle_one_to_one():
    return 'one to one : int or float'

def handle_list_to_one():
    return 'List to one'

def validate_input(input, output):

    cls_int, cls_float, cls_str = "<class 'int'>", "<class 'float'>", "<class 'str'>"
    in_type, out_type = str(type(input)), str(type(output))

    if in_type in [cls_int, cls_float]:
        if out_type in [cls_int, cls_float]:
            return handle_one_to_one()
        else:
            error = "Sorry, When Input type is int/float output should be similar type !!"
            return error
    elif in_type == cls_str:
        error = "Sorry, I do not support scalar String data as INPUT at this time!!"
        return error

    in_types = [str(type(x)) for x in input]
    in_length = len(set(in_types))
    in_set = "".join(set(in_types))  # join as one single string so easy to compare below

    valid_input = in_set == cls_int or in_set == cls_float or \
                  in_set == cls_float+cls_int or in_set == cls_int+cls_float
    error = ''
    if cls_str in in_types:
        error = "Sorry, I do not support String data as part of  INPUT List at this time!!"
        return error

    # at this point in flow INPUT  is valid LIST, if OUTPUT is single value, call the handle function,
    if out_type in [cls_int, cls_float]:
        return handle_list_to_one()
    else:
        error = "call other routines, it may be fizz buzz like INPUT number list, output mix list"
        #return fizz_buzz()
        return error

    #return error


# in sever*dbc file instaed of a , make it grades =
grades = [ 'xyz', ['abc'], [ 80, 'abc'], [80, '95'], \
           [80, '95', 76], [80, '95', 76.5], \
           22, 34.5, [80], [80, 79, 67, 90, 85], \
           [ 33.33, 89,44.6],  [ 44.5, 22.6] ]

output = [ 'xyz', ['abc'], [ 80, 'abc'], [80, '95'], \
           [80, '95', 76], [80, '95', 76.5], \
           44, -20, [80], 90, \
           33.33,  67.1 ]

for i in range(len(grades)):
    r = validate_input(grades[i], output[i])
    print( grades[i], output[i], r)

