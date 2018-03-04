from flask import Flask, render_template, request
from runcode import runcode
app = Flask(__name__)

@app.route("/hi", methods=['POST', 'GET'])
def handle_hi():
    if request.method == 'GET':
        name = "Gitu"
        text = render_template("hi.html",
                               target="handle_hi",
                               greet = name)
        return text
    else:
        name = request.form['name']
        age = int(request.form['age'])
        if age < 18:
            message = "sorry, you have to wait till 18 to drive"
        else:
            message = "Hurry!!!!!!, you can drive"

        text = render_template("hi_response.html",
                               target="handle_hi",
                               name = name,
                               message = message)
        return text


@app.route("/bye")
def bye():
    text = render_template("bye.html")
    return text


if __name__ == "__main__":
    app.run(debug=True)   # this debug flag detects "code file chagnes & start Flash server automatically"
    #app.run()
