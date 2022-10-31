from flask import Flask
from flask import request, redirect, url_for, render_template

app = Flask(__name__)

database= {}

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form.to_dict()
        database[data["name"]] = data
        return redirect(url_for("dashboard", name=data["name"]))
    if request.method == "GET":
        return render_template("registration.html")

@app.route("/dashboard/?<name>", methods=["GET"])
def dashboard(name):
    return render_template("dashboard.html", name=name, email=database[name]["email"], phone=database[name]["phone"])