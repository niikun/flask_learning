from flask import Flask
from flask import render_template

app = Flask(__name__)

test_list = [
    "test1",
    "test2",
    "test3",
    "test4",
    "test5",
    "test6",
    "test7",
]


@app.route("/<name>")
def index(name):
    return render_template("index.html", name=name, items=list)


if __name__ == "__main__":
    app.run()
