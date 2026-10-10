from flask import Flask

app = Flask("__name__")

@app.route("/")
def hola_mundo():
    return "<h1 style=\"color: blue; font-size: 40px;\">¡Hola Mundo desde Flask!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

