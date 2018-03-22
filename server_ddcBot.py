from flask import Flask, render_template, request


# ------------------- application specific imports
from app import execute_pycode as execpycode
from app import examples_pycode as example

app = Flask(__name__)


default_rows = "40"  # 15   , 18
default_cols = "90"   # 60

@app.route("/")
@app.route("/examples")
@app.route("/py")
@app.route("/runpy", methods=['POST', 'GET'])
def runpy():
    if request.method == 'POST':
        code = request.form['code']
        submit_type = request.form['button1']
        run = execpycode.RunPyCode(code)
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
            num = '2_1'

        code = eval('example.excode' + num)
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
