from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur l'API Flask !"

@app.route("/api/data")
def get_data():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST", "localhost"),
            user=os.getenv("DATABASE_USER", "root"),
            password=os.getenv("DATABASE_PASSWORD", ""),
            database=os.getenv("DATABASE_NAME", "testdb")
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT 'Hello from MySQL!' AS message")
        result = cursor.fetchone()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)