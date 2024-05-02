from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    lista_nombres = ["Hvera", "Maxi", "Edgarplank", "Dperrete", "Kiritsuna", "Spynck"]
    return render_template("home.html", nombres=lista_nombres)

@app.route("/djperrete")
def perfil_djperrete():
    return render_template("djperrete.html")

@app.route("/hvera")
def perfil_hvera():
    return render_template("hvera.html")

@app.route("/maxi")
def perfil_maxi():
    return render_template("maxi.html")

@app.route("/edgarplank")
def perfil_edgarplank():
    return render_template("edgarplank.html")

@app.route("/kiritsuna")
def perfil_kiritsuna():
    return render_template("kiritsuna.html")

@app.route("/spynck")
def perfil_spynck():
    return render_template("spynck.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)