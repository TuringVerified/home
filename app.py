from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
