from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template("list_prof.html", list=list)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
