from flask import Flask, render_template
import subprocess
import shutil
import os

app = Flask(__name__)

VISITOR_FILE = "data/visitors.txt"

def VisitorCount():
    if not os.path.exists(VISITOR_FILE):
        os.makedirs("data", exist_ok=True)
        with open(VISITOR_FILE, "w") as f:
            f.write("0")
    with open(VISITOR_FILE, "r") as f:
        return int(f.read())
    
def IncVisitorCount():
    count = VisitorCount() + 1
    with open(VISITOR_FILE, "w") as f:
        f.write(str(count))
    return count


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