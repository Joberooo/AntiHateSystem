from flask import Flask, render_template

app = Flask(__name__)


@app.route("/settings")
def settings():
    return render_template("settings.html", conten=None)


@app.route("/hate")
def hate():
    return render_template("hate.html", content=None)


@app.route("/clientPanel")
def client():
    return render_template("clientPanel.html", content=None)


@app.route("/loginPanel")
def login():
    return render_template("login.html", content=None)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
