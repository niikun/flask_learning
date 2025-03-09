from flask import Flask,render_template,session,request,redirect,url_for
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

key = os.getenv("SECRET_KEY")
app.secret_key = key

id_pwd = {"niikun":"1234"}

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if id_pwd.get(username) == password:
            session["username"] = username
            return redirect(url_for("index"))
        return "Login failed"
    else:
        return render_template("login.html")

@app.route("/session")
def show_session():
    return f"Current session: {session.get('username')}"

if __name__ == "__main__":
    app.run(debug=True)
