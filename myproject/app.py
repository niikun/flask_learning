from flask import Flask
from flask import render_template

app = Flask(__name__)

contents = [
    {"id":1, "title":"title1", "body":"body1"},
    {"id":2, "title":"title2", "body":"body2"},
    {"id":3, "title":"title3", "body":"body3"},
]

@app.route('/')
def top():
    return render_template('index.html',contents=contents)


if __name__=="__main__":
    app.run(debug=True)