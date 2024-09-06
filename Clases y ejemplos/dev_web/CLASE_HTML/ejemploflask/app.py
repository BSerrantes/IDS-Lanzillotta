from flask import Flask, render_template

PORT = 8080

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', year=2024)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)