from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

if __name__ == "__main__":
    app.run(debug=True)