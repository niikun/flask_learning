from flask import Flask
from flask import render_template

app = Flask(__name__)


memo_list = [
    ["memo1","content1"],
    ["memo2","content2"],
    ["memo3","content3"]
]

@app.route("/")
def top():
    return render_template("index.html",memo_list=memo_list)

if __name__=="__main__":
    app.run(debug=True)