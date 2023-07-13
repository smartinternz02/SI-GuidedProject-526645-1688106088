from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/portfolio-details.html')
def dashboard():
    return render_template("portfolio-details.html")

if __name__ == "__main__":
    app.run(debug=False, port=5500)
