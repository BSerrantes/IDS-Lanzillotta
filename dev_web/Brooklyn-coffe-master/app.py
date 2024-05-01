from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("fname")
        email = request.form.get("femail")
        message = request.form.get("fmessage")

        print(name, email, message)

    return render_template('contact.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/menu")
def menu():
    lista = {}
    return render_template('menu.html', lista=lista)

@app.route("/reservation")
def reservation():
    return render_template('reservation.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)