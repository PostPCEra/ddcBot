from flask import Flask, render_template, request
from runcode import runcode
app = Flask(__name__)

default_py_code = """import sys
import os

a = [ 1, 3, 4]
b = [ 2, 6, 8]

# @input = a ; @output = b
"""

default_rows = "15"
default_cols = "60"

@app.route("/")
@app.route("/py")
@app.route("/runpy", methods=['POST', 'GET'])
def runpy():
    if request.method == 'POST':
        code = request.form['code']
        run = runcode.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = "No compilation for Python"

    #resrun = resrun + '\n# newly added line'
    code = code + '\n' + resrun

    return render_template("main.html",
                           code=code,
                           target="runpy",
                           resrun=resrun,
                           rescomp=rescompil,#"No compilation for Python",
                           rows=default_rows, cols=default_cols)

if __name__ == "__main__":
    app.run()
