from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text,create_engine
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:12345@localhost:3306/articulos")

def obtener_articulos():
    conn = engine.connect()
    query = f"Select * from art;"

    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    
    data = []

    for row in result:
        producto = {
            'id': row.id,
            'description': row.description,
            'price': row.price
        }
        data.append(producto)

    return data

def obtener_articulo(id):
    conn = engine.connect()
    query = f"select * from art where id = {id};"
    
    try:
        result = conn.execute(text(query))
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    
    if result.rowcount != 0:

        row = result.first()
        articulo ={
            'id' : row.id,
            'description': row.description,
            'price': row.price    
        }
        return articulo
    
    return jsonify({"message": "El Producto no existe"}), 404
    



def crear_producto(product_data):
    conn = engine.connect()
    query = f"Insert into art(id,description,price) values({product_data['id']},{product_data['description']},{product_data['price']});"
    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__)) 
    
    return jsonify({"message": "producto agregado exitosamente"})

def eliminar_producto(product_id):
    conn = engine.connect()
    query = f"delete from art where id = {product_id}"

    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    
    return jsonify({"message":"Se ha borrado la fila en forma satisfactoria."})

def editar_producto(product_data, product_id):
    conn = engine.connect()
    query = f"update art set id = {product_data['id']}, description = {product_data['description']}, price = {product_data['price']} where id = {product_id};"

    try:
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
        return jsonify(str(err.__cause__))
    
    return jsonify({"message": "producto modificado exitosamente"})

