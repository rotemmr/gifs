from flask import Flask, render_template
from dotenv import load_dotenv
import os
import fcntl
import mysql.connector

app = Flask(__name__)

#load_dotenv()

#DB_HOST = os.getenv("DB_HOST")
#DB_USER = os.getenv("DB_USER")
#B_PASSWORD = os.getenv("DB_PASSWORD")
#DB_NAME = os.getenv("DB_NAME")
#
#def get_db_connection():
#    return mysql.connector.connect(
#        host=DB_HOST,
#        user=DB_USER,
#        password=DB_PASSWORD,
#        database=DB_NAME,
#    )

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

