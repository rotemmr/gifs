from flask import Flask, render_template
import subprocess
import shutil
import os
import mariadb
import fcntl

app = Flask(__name__)

def get_db_connection():
    connection = mariadb.connect(
        host='35.194.26.110',  
        user='root',               
        password='12481478Rr',  
        database='myapp'           
    )
    return connection



VISITOR_FILE = "data/visitors.txt"

def VisitorCount():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM visitors")
        result = cursor.fetchone() 
        cursor.close()
        connection.close()
        return result[0] if result else 0
    except mariadb.Error as e:
        print(f"Error connecting to database: {e}")
        return 0

def IncVisitorCount():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO visitors (id) VALUES (NULL)")
        connection.commit()  
        cursor.close()
        connection.close()
        return VisitorCount()
    except mariadb.Error as e:
        print(f"Error connecting to database: {e}")
        return VisitorCount()


@app.route("/")
def home():
    version = os.getenv("VERSION", "1.0.0")
    VISITOR_COUNT = IncVisitorCount()
    return render_template("homepage.html", version=version, count = VISITOR_COUNT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# def get_git_version():
#    try:
#        git_path = shutil.which("git")
#        if git_path is None:
#           raise FileNotFoundError("Git is not installed or not found in PATH.")
#        
#       # latest tag in repo
#        version = subprocess.check_output([git_path, "describe", "--tags", "--abbrev=0"]).strip().decode()
#        
#        print(f"Git Version: {version}")
#        
#        return version
#    except subprocess.CalledProcessError:
#        # default when theres no tag
#        return "1.0.0"
#   except FileNotFoundError:
#        return "Git not found"