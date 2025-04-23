import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        db_host = os.getenv("DATABASE_HOST", "localhost")
        conn = mysql.connector.connect(
            host=db_host,
            user="root",
            password="rootpassword",
            database="testdb"
        )
        return "Connexion réussie à la base de données !"
    except Exception as e:
        return f"Erreur de connexion : {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)