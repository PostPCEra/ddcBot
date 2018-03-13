from flask import Flask, render_template, request
from runcode import runcode
app = Flask(__name__)


excode0 = """import sys
import os

a = [ 1, 3, 4]
b = [ 2, 6, 8]

# @input = a ; @output = b
"""

excode1 = """import sys
import os

height = [2, 6, 7] 
weight = [10, 30, 35]

# @input = height ; @output = weight
"""

excode2 = """import sys
import os

cat_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
cat_out = [5, 6, 'fizz', 8, 'buzz', 'fizz', 11, 12, 'fizz','buzz']

# @input = cat_in ; @output = cat_out
"""

excode3 = """import sys
import os

cat_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
cat_out = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14]

# @input = cat_in ; @output = cat_out
"""

excode4 = """import sys
import os

seq_in = [2, 6,12, 13,15, 19, 20, 58] 
seq_out = ['child', 'child', 'child', 'teen', 'teen', 'teen', 'adult', 'adult']

# @input = seq_in ; @output = seq_out
"""

excode5 = """import sys
import os

date1 = '2018-01-15'
date2 = '2018-04-18'

# @input = date1 ; @output = date2
"""

excode6 = """import sys
import os
import math

a = [2, 3, 5, 6]
b = [8, 27, 125,  216]

# @input = a ; @output = b
"""
 
excode7 = """import sys
import os
import math

a = [8, 27, 125,  216] 
b = [2, 3, 5, 6]

# @input = a ; @output = b
"""

default_rows = "15"
default_cols = "60"

@app.route("/")
@app.route("/examples")
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
        num = request.args.get('ex')
        if num is None:
            num = '0'

        code = eval('excode' + num)
        resrun = 'No result!'
        rescompil = "No compilation for Python"

    return render_template("main.html",
                           code=code,
                           target="runpy",
                           resrun=resrun,
                           rescomp=rescompil,#"No compilation for Python",
                           rows=default_rows, cols=default_cols)

if __name__ == "__main__":
    # good Cache article : http: // brunorocha.org / python / flask / using - flask - cache.html
    #app.config["CACHE_TYPE"] = "null"

    app.run(debug=True)   # this debug flag detects "code file chagnes & start Flash server automatically"
    #app.run()
