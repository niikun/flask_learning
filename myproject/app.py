from flask import Flask, render_template, g ,request ,redirect # type: ignore
import sqlite3
DATABASE = "flaskmemo.db"

app = Flask(__name__)

# database
def connect_db():
    rv = sqlite3.connect(DATABASE) # sqlite3.connect()でデータベースに接続
    rv.row_factory = sqlite3.Row  # sqlite3.Rowオブジェクトを使って行を取得する
    return rv

def get_db():
    # g.sqlite_dbが存在しない場合はconnect_db()を呼び出してデータベースに接続
    if not hasattr(g, "sqlite_db"): 
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.route('/')
def top():
    memo_list = get_db().execute('SELECT id, title, body FROM memo').fetchall()
    return render_template('index.html', memo_list=memo_list)

@app.route('/regist', methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        db = get_db()
        db.execute('INSERT INTO memo (title, body) VALUES (?, ?)', [title, body])
        db.commit()
        return redirect('/')
    
    return render_template('regist.html')

if __name__ == "__main__":
    app.run(debug=True)