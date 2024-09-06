from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def Home():
    Nombre = "Bryan"
    Apellido = "Serrantes" 
    return render_template("home.html", nombre=Nombre, apellido=Apellido)

@app.route("/recetas")
def Recetas():
    datos = {"1":
             {"nombre":"Budín de pan",
              "descripción":"El mejor budín de pan...",
              "preparación":"Incorporar el pan de miga...",
              "ingredientes":{"Pan de miga":"250gr","Leche tibia":"750cc","Huevos":"3"}},
              "2":
              {"nombre":"Chocotorta",
               "descripción":"La chocotorta origial",
               "preparación":"Con las galletitas...",
               "ingredientes":{"Dulce de leche":"350gr","Crema":"350cc","Galletitas de chocolate":"700gr","Cacao en polvo":"50gr"}},
               "3":
               {"nombre":"Pasta frola",
                "descripción":"La pastafrola de la abuela",
                "preparación":"Incorporar el huevo, la yema ...",
                "ingredientes":{"Huevo":"1","Yema":"1","Azucar":"200gr","Manteca":"250gr","Dulce de batata":"400gr"}}
            }

    return render_template("recetas.html", recetas=datos)

@app.route("/mireceta/<id>")
def Mireceta(id):
    nro_receta_elegida = id

    datos = {"1":
             {"nombre":"Budín de pan",
              "descripción":"El mejor budín de pan...",
              "preparación":"Incorporar el pan de miga...",
              "ingredientes":{"Pan de miga":"250gr","Leche tibia":"750cc","Huevos":"3"}},
              "2":
              {"nombre":"Chocotorta",
               "descripción":"La chocotorta origial",
               "preparación":"Con las galletitas...",
               "ingredientes":{"Dulce de leche":"350gr","Crema":"350cc","Galletitas de chocolate":"700gr","Cacao en polvo":"50gr"}},
               "3":
               {"nombre":"Pasta frola",
                "descripción":"La pastafrola de la abuela",
                "preparación":"Incorporar el huevo, la yema ...",
                "ingredientes":{"Huevo":"1","Yema":"1","Azucar":"200gr","Manteca":"250gr","Dulce de batata":"400gr"}}
            }
    return render_template("mireceta.html", id= nro_receta_elegida, recetas=datos)


if __name__ == "__main__":
    app.run("127.0.0.1",port="8080", debug=True)