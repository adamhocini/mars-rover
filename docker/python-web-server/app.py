from flask import Flask

app = Flask(__name__)


@app.route("/new")
def new_route():
    return "Ceci est une nouvelle route !"

@app.route("/")
def home():
    return "Bienvenue sur mon serveur web Python !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)