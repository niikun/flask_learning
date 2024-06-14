from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def hello_name(name):
    text = f"Hello, {name}"
    return text

if __name__=="__main__":
    app.run(debug=True)