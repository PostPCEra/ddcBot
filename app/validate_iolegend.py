
from app import global_const as gc
from app import application_errors as aerr

# ------------------------ extract_input_output_names ----------------------------------------------
#
def extract_input_output_names(code):

    import re
    from traceback import print_exc

    code_lines = code.split("\n")
    ioline = ""
    for line in code_lines:
        if '@input' in line:
            ioline = line
            break;

    error = ''  # init
    try:
        if not ('@input' in ioline and '@output' in ioline):
            raise MyNoInputException("Legend missing")

        text_part1, text_part2 = ioline.split(";")  # handled by 'ValueError' exception

        # use [ ?] , [\w] gives less empty string matches instead of ( ?) , (\w)
        regex2 = r"output([ ?]*)=([ ?]*)([\w]+)"
        matches = re.findall(regex2, text_part2)
        print(str(matches[0]))
        output_symbol = str(matches[0][2])

        parts_for_input = text_part1.split(",")  # if no ',' then it just return whole string
        regex1 = r"input([ ?]*)=([ ?]*)([\w]+)"
        matches = re.findall(regex1, parts_for_input[0])
        print(str(matches[0]))
        input_symbol = str(matches[0][2])

        input2_symbol = ''
        if len(parts_for_input) > 1:  # if second input parmeter exists, then only extract it
            input2_symbol = parts_for_input[1]

        print(input_symbol, output_symbol, input2_symbol)

    except Exception as e:
        type = e.__class__.__name__
        if type == 'MyNoInputException':
            error = aerr.msg('E_IOL1_MISSING_WORDS')
        elif type == 'ValueError':
            error = aerr.msg('E_IOL2_SEPCHAR')
        else:
            error = aerr.msg('E_IOL0_UNKONWN')
        #print(type)
        #print_exc()

    if error == '':
        # first 2 params as symbols '{}', next 2 as value
        code_str = "\n\n# --------------------- main program call generated by runcode.py--------------------------\n" + \
                   "code = main_entry_point('{}' , '{}', {}, {}, '{}')\n".format(input_symbol, output_symbol,
                                                                           input_symbol, output_symbol, input2_symbol) + \
                   "print(code)\n\n"  # print() will sends to stadout which in tern get back to browser
    else:
        code_str = error

    return code_str  # this code_str is written into a.out file , see contents

