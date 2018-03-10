import sys
import os
#sys.path.append(os.path.abspath("/Users/padma/ddcBot/running"))
from bot_algo import *

# --------------------------------------
def main():

    test_suite = [  ([1, 5, 8], [6, 10, 13]),
                    ([2, 6, 7], [10, 30, 35]),
                    (list(range(1, 15)), [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14] ),
                    (list(range(1, 11)), [5, 6, 'fizz', 8, 'buzz', 'fizz', 11, 12, 'fizz','buzz']),
                    ([2, 6,12, 13,15, 19, 20, 58], ['child', 'child', 'child', 'teen', 'teen', 'teen', 'adult', 'adult']),

                    ([{'name': 'asr', 'grade': 45}, {'name': 'pad', 'grade': 40}, {'name': 'gitu','grade': 15}, {'name': 'anv', 'grade': 20}],
                      [{'name': 'gitu', 'grade': 15}, {'name': 'anv', 'grade': 20}])
                 ]

    #for pair in test_suite[3:4]:  # by simpy changing index, we can selectively feed the test cases we like
    for pair in test_suite[:5]:

        input_as_value, output_as_value = pair
        code = main_entry_point('input_dummy_g', 'output_dummy_g', input_as_value, output_as_value)
        print(code)

# -------------------  main -------------------
#
code = main()

