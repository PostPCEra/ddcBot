import subprocess
import sys
import os

class RunPyCode(object):
    
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="a.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result


    def extract_input_output_names(self, code):
        code_lines = code.split("\n")
        ioline = ""
        for line in code_lines:
            if '@input' in line:
                ioline = line
                break;

        elm = ioline.split(";")
        input_var = elm[0].split('=')[-1]
        output_var = elm[1].split('=')[-1]

        input, output = input_var.strip(), output_var.strip()
        # first 2 params as symbols '{}', next 2 as value
        code_str = "main_entry_point('{}' , '{}', {}, {})\n".format(input, output, input, output)
        return code_str

    def run_py_code(self, submit_type, code=None):
        filename = "./running/a.py"
        if not code:
            code = self.code

        with open(filename, "w") as f:
            f.write(code)  # user entered coded from the editor

            if submit_type == 'Invoke Bot':
                botcode = open('./running/bot_algo.py', 'r').read()
                f.write(botcode)  # and ADD botcode that is is our alog code from bot_algo.py file

                main_call_code = self.extract_input_output_names(code)
                f.write(main_call_code)

        self._run_py_prog(filename)
        return self.stderr, self.stdout

