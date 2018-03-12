import sys
import os
#sys.path.append(os.path.abspath("/Users/padma/ddcBot/running"))
from bot_algo import *

# --------------------------------------
def main():

    test_suite = [ { 'case':'.0 Dates', 'data': ('2018-01-15', '2018-04-18') },
    { 'case':'1.0 Arthimatic Sequence', 'data': ([1, 5, 8], [6, 10, 13]) },
    {'case': '1.1 Arth negative data', 'data': ([1, 5, 8], [-7, -3, 10])},
    {'case': '1.2 Arth one missing', 'data': ([2, 6, 7], [8, 12, 9])},

    {'case': '2.0 Geometric Sequence', 'data': ([2, 6, 7], [10, 30, 35])},
    {'case': '2.1 Geometric Sequence', 'data': ([2, 6, 7], [-10, -30, -35])},
    {'case': '2.1 Geometric one missing', 'data': ([2, 6, 7], [-10, -30, -30])},

    {'case': '3.0 FizzBuzz like category',
     'data': (list(range(1, 15)), [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14] )},
    {'case': '3.1 FizzBuzz 2',
     'data': (list(range(1, 11)), [5, 6, 'fizz', 8, 'buzz', 'fizz', 11, 12, 'fizz','buzz'])},

    {'case': '4.0 Range Category',
     'data':([2, 6,12, 13,15, 19, 20, 58], ['child', 'child', 'child', 'teen', 'teen', 'teen', 'adult', 'adult'])},

    {'case': '5.0 Filter',
     'data': ([{'name': 'asr', 'grade': 45}, {'name': 'pad', 'grade': 40}, {'name': 'gitu','grade': 15}, {'name': 'anv', 'grade': 20}],
                      [{'name': 'gitu', 'grade': 15}, {'name': 'anv', 'grade': 20}])}
    ]

    #for pair in test_suite[3:4]:  # by simpy changing index, we can selectively feed the test cases we like
    for row in test_suite[:2]:

        log.debug('------------{}\n'.format(row['case']))
        input_as_value, output_as_value = row['data']
        code = main_entry_point('input_dummy_g', 'output_dummy_g', input_as_value, output_as_value)
        print(code)

# -------------------  main -------------------
#
code = main()
a= 4
#import os
#os.system('chmod 777 log-4*')

