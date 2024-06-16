from flask import Flask
from flask import render_template

app = Flask(__name__)

memo_list = [
    {"title":"memo1","content":"content1"},
    {"title":"memo2","content":"content2"}
]

@app.route("/")
def top():
    return render_template("index.html",memo_list=memo_list)

if __name__=="__main__":
    app.run(debug=True)