
# -------------------------------------------------------------------------------------------------------
# pytest tutorial : http://pythontesting.net/framework/pytest/pytest-introduction/

# How to run tests :
# be in test dir
# $py.test -v  <test-file.py>  or  $python -m pytest -v  <test-file.py>
# ---------------------------------------------------------------------------------------------------------
import sys
sys.path.append('../')

from app import validate_iolegend as iolegend

CODE_SAMPLE = ''

def setup_module(module):
    print("setup_module      module:%s" % module.__name__)

    sample = """import sys
    import os

    weight = [2, 6, 7] 
    height = [10, 30, 35]
    
    """

    global CODE_SAMPLE
    CODE_SAMPLE = sample


def test_at_input_ouput():
    code = CODE_SAMPLE + '# area=abc  @output=  0varout'
    retcode = iolegend.extract_input_output_names(code)
    assert 'E_IOL1_MISSING_WORDS' in retcode

def test_missing_separator():
    code = CODE_SAMPLE + '#@input=abc  @output=  0varout'
    retcode = iolegend.extract_input_output_names(code)
    assert 'E_IOL2_SEPCHAR' in retcode

