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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INT PRIMARY KEY AUTO_INCREMENT,
            count INT NOT NULL
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM visitors")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO visitors (count) VALUES (0)")
    
    conn.commit()
    cursor.close()
    conn.close()

VISITOR_FILE = "data/visitors.txt"

def VisitorCount():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(VISITOR_FILE):
        with open(VISITOR_FILE, "w") as f:
            f.write("0")

    try:
        with open(VISITOR_FILE, "r") as f:
            count = f.read().strip()
            return int(count) if count.isdigit() else 0
    except ValueError:
        return 0

def IncVisitorCount():
    count = VisitorCount() + 1

    with open(VISITOR_FILE, "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        f.write(str(count))
        f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)

    return count


@app.route("/")
def home():
    version = os.getenv("VERSION", "1.0.0")
    VISITOR_COUNT = IncVisitorCount()
    return render_template("homepage.html", version=version, count = VISITOR_COUNT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
