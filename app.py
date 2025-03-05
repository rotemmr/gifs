from flask import Flask, render_template
import mysql.connector
import subprocess
import shutil
import os
import fcntl

app = Flask(__name__)

#MySQL Creds
DB_CONFIG = {
    "host": os.getenv("DB_HOST",),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    #Visitors Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INT PRIMARY KEY AUTO_INCREMENT,
            count INT NOT NULL
        )
    """)

    #Dog Gifs Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dog_gifs (
            id INT PRIMARY KEY AUTO_INCREMENT,
            gif_url VARCHAR(255) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM visitors")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO visitors (count) VALUES (0)")
    
    conn.commit()
    cursor.close()
    conn.close()


@app.route("/")
def home():
    version = os.getenv("VERSION", "1.0.0")
    return render_template("homepage.html", version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
