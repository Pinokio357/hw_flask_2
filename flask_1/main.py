from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def ind():
    return render_template("index.html")


@app.route("/cloth.html/")
def clt():
    return render_template("cloth.html")


@app.route("/empty.html/")
def emp():
    return render_template("empty.html")


@app.route("/cloth.html/jacket.html/")
def jct():
    return render_template("jacket.html")


@app.route("/cloth.html/empty.html/")
def emp_2():
    return render_template("empty.html")


if __name__ == "__main__":
    app.run(debug=True)