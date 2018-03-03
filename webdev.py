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
        submit_type = request.form['button1']
        run = runcode.RunPyCode(code)
        rescompil, resrun = run.run_py_code(submit_type, code)
        if not resrun:
            resrun = 'No result!'

        if submit_type == 'Invoke Bot':
            code = code + '\n' + resrun
            resrun = '' # do not display any thing on RUN window
        elif submit_type == 'Launch':
            pass  # do nothing
    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = "No compilation for Python"

    return render_template("main.html",
                           code=code,
                           target="runpy",
                           resrun=resrun,
                           rescomp=rescompil,#"No compilation for Python",
                           rows=default_rows, cols=default_cols)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run()
