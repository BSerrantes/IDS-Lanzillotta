from flask import Flask,render_template,request,redirect,url_for
from api import *

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Bryan"
    apellido = "Serrantes"
    return render_template("home.html", name=nombre, lastname=apellido)

@app.route('/listado')
def listado():
    product_list = obtener_articulos()
    return render_template("listado.html", articulos=product_list)

@app.route('/formulario', methods=["GET","POST"])
def formulario():
    if request.method == "POST":
        product_id = request.form.get("fid")
        product_description = request.form.get("fdescription")
        product_price = request.form.get("fprice")

        product_data ={
            'id' : product_id,
            'description': product_description,
            'price': product_price
        }
        crear_producto(product_data)
        return redirect(url_for('listado'))
    return render_template("formulario.html")

@app.route('/delete_<product_id>')
def delete_product(product_id):
    eliminar_producto(product_id)
    return redirect(url_for('listado'))

@app.route('/editar_producto/<id>', methods=["GET","POST"])
def edit_product(id):
    old_id = id
    articulo = obtener_articulo(old_id)

    if request.method == "POST":
        product_id = request.form.get("fid")
        product_description = request.form.get("fdescription")
        product_price = request.form.get("fprice")

        product_new_data ={
            'id' : product_id,
            'description': product_description,
            'price': product_price
        }
        editar_producto(product_new_data, old_id)
        return redirect(url_for('listado'))
    return render_template("update_form.html", pr_id = old_id, art = articulo)

if __name__ == "__main__":
    app.run(debug=True)