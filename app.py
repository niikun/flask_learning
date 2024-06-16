from flask import Flask
from flask import render_template

app = Flask(__name__)


memo = [
    ["memo1","content1"],
    ["memo2","content2"],
    ["memo3","content3"]
]

@app.route("/")
def top(memo=memo):
    return render_template("index.html",memo=memo)

if __name__=="__main__":
    app.run(debug=True)