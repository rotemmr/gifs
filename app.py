from flask import Flask, render_template
import subprocess
import shutil

app = Flask(__name__)

def get_git_version():
    try:
        git_path = shutil.which("git")
        if git_path is None:
            raise FileNotFoundError("Git is not installed or not found in PATH.")
        
        # latest tag in repo
        version = subprocess.check_output([git_path, "describe", "--tags", "--abbrev=0"]).strip().decode()
        
        print(f"Git Version: {version}")
        
        return version
    except subprocess.CalledProcessError:
        # default when theres no tag
        return "1.0.0"
    except FileNotFoundError:
        return "Git not found"

@app.route("/")
def home():
    version = get_git_version()
    return render_template("homepage.html", version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)