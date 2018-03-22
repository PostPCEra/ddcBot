import subprocess
import sys
import os
import re


from app.global_const import *
from app import validate_input

class MyNoInputException(Exception):
    pass

class RunPyCode(object):
    
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="./app/_generatedcode.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result




    # ------------------------ run_py_code ----------------------------------------------
    #
    def run_py_code(self, submit_type, code=None):
        filename = "./app/_generatedcode.py"
        if not code:
            code = self.code

        with open(filename, "w") as f:
            f.write(code)  # user entered coded from the editor

            if submit_type == 'Invoke Bot':
                botcode = open('./running/bot_algo.py', 'r').read()
                f.write(botcode)  # and ADD botcode that is is our alog code from bot_algo.py file

                main_call_code = validate_input.extract_input_output_names(code)
                f.write(main_call_code)
                if 'Error:****' in main_call_code:
                    return main_call_code, main_call_code  # return error to both std_err, std_out

        self._run_py_prog(filename)

        std_err, std_out = self.stderr, self.stdout
        #std_out = ERROR_NOT_ARTHIMETIC_GEOMETRIC
        if std_out in ERROR_LIST:
            std_err = std_out
            std_out = ''

        return std_err, std_out

