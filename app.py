from flask import Flask, render_template
import subprocess

app = Flask(__name__)

def get_git_version():
    try:
        # latest tag in repo
        version = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).strip().decode()
        return version
    except subprocess.CalledProcessError:
        # default when theres no tag
        return "1.0.0"

@app.route("/")
def home():
    version = get_git_version()
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)