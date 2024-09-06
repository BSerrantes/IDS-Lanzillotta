from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def Home():
    Nombre = "Bryan"
    Apellido = "Serrantes" 
    return render_template("home.html", nombre=Nombre, apellido=Apellido)

@app.route("/datos_personales",methods=["GET","POST"])
def Formulario():
    if request.method == "POST":
        nombre = request.form.get("fnombre")
        apellido = request.form.get("fapellido")
        celular = request.form.get("fcelular")
        direccion = request.form.get("fdirec")
        dni = request.form.get("fdni")
        lista_datos = [nombre, apellido, celular, direccion, dni]
        
        return render_template("aceptado.html", datos=lista_datos)

    return render_template("formulario.html")

@app.route("/aceptado")
def Aceptado():
    return render_template("aceptado.html")

if __name__ == "__main__":
    app.run("127.0.0.1",port="8080", debug=True)
