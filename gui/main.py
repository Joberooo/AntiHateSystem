from flask import Flask, render_template

app = Flask(__name__)


@app.route("/loginPanel")
def login():
    return render_template("login.html", content=None)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
