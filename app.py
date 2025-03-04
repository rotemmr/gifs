from flask import Flask, render_template
import subprocess
import shutil
import os
import fcntl

app = Flask(__name__)

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