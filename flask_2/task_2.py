#Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
#На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/login/", methods=["POST"])
def login():
    name = request.form["name"]
    emale = request.form["emale"]
    response = make_response(render_template("hello.html", name=name))
    response.set_cookie("name", name)
    response.set_cookie("emale", emale)
    return response


@app.route("/exit/")
def exit():
    response = make_response(redirect(url_for("form")))
    response.set_cookie("name", " ", 0)
    response.set_cookie("emale", " ", 0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
