import os

from flask import Flask, abort, render_template, send_file, send_from_directory

app = Flask(__name__)

# Default CV location can be overridden with CV_FILE_PATH env var.
CV_FILE_PATH = os.environ.get("CV_FILE_PATH", os.path.join(app.root_path, "private_assets", "cv.pdf"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

@app.route("/pgp")
def pgp():
    return render_template("pgp.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, "robots.txt")

@app.route("/blog/omen-drivers")
def blog_omen():
    return render_template("blog_omen.html")


@app.route("/cv")
def cv():
    if not os.path.exists(CV_FILE_PATH):
        abort(404)
    return send_file(CV_FILE_PATH, mimetype="application/pdf", download_name="cv.pdf")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
