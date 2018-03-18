#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -----------------  extract_input_output_names  -------------------
# https://stackoverflow.com/questions/4730435/exception-passing-in-python
#
def extract_input_output_names(text_str):
    import re
    from traceback import print_exc

    error = ''
    try:
        text_part1, text_part2 = text_str.split(";")

        # use [ ?] , [\w] gives less empty string matches instead of ( ?) , (\w)
        regex2 = r"output([ ?]*)=([ ?]*)([\w]+)"
        matches = re.findall(regex2, text_part2)
        print(str(matches[0]))
        output = str(matches[0][2])

        parts_for_input = text_part1.split(",")
        regex1 = r"input([ ?]*)=([ ?]*)([\w]+)"
        matches = re.findall(regex1, parts_for_input[0])
        print(str(matches[0]))
        input = str(matches[0][2])

        print(input, output)

    except Exception as e:
        type = e.__class__.__name__
        print(type)
        if type == 'ValueError':
            error = "***********------The separator ; is missing in the input output legend"
        else:
            print('***********------ some other different exception occured ')
        print(error)
        print_exc()
        return 0

# main call
test_suite = [  ['output has: no separator char ; ', "# @input=a  @output=  1varout"],
        ["output has: left & right one space", "# @input=a ; @output = 2varout"],
        ["output has: left & right zero spaces", "# @input=a ; @output=3varout"],
        ["output has: left & right zero spaces and spaces at the END", "# @input=a ; @output=4varout  "],
        ["output has: left & right one+ spaces", "# @input=a ; @output  =   5varout"],
        ["output has: left & right one+ spaces, and spaces at the END", "# @input=a ; @output  =   6varout  "],
        ["output has: left spaces", "# @input=a ; @output  =7varout"]
    ]

for row in test_suite[:]:
    print("-------------", row[0], ":", row[1])
    #print(row[0], ":", row[1].split(";")[1])
    extract_input_output_names(row[1])


# ([.\w]+)(?:,([.\w]+))?
# for  a,obj.name