from flask import Flask, render_template
#, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_msg():
    name = ["Seba","Bryan","Dani"]
    return render_template("home.html", nombres = name)

@app.route("/perfil")
def perfil():
    return render_template("mi_perfil.html", nombre = "Juan")

if __name__ == "__main__":
    app.run(port=8080,debug = True)