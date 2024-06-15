from flask import Flask
from flask import render_template

app = Flask(__name__)

name_list = [
    "Alice",
    "Bob",
    "Cathy",
    "David"
]

@app.route("/<name>")
def hello(name):
    return render_template("index.html",name=name,name_lists=name_list)

if __name__=="__main__":
    app.run(debug=True)