from flask import Flask, render_template, request
import sqlite3

#cur.execute needed first to establish the table

sql = '''CREATE TABLE IF NOT EXISTS Chat (id INTEGER PRIMARY KEY, msg TEXT)'''

def sendSQL(sql):
    db = sqlite3.connect("./chat.db")
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()

def getData():
    db = sqlite3.connect("./chat.db")
    cur = db.cursor()
    sql = '''SELECT * FROM Chat'''
    cur.execute(sql)
    db.commit()
    results = cur.fetchall()
    db.close()
    return results

app = Flask(__name__)

name = "Bart"

# @ = decorator to establish page.  Expects a function defined next
@app.route('/')
def index():
    return "hello World"


@app.route('/chat', methods=['GET','POST'])
def chat():
    chatroom = getData()
    if request.method == "GET":
        print("get request")
    elif request.method=="POST":
        sql='''INSERT INTO Chat (msg) VALUES ("{}")'''.format(request.form["message"])
        sendSQL(sql)
    chatroom = getData()
    return render_template("chat.html", user=name, chatroom=chatroom)

app.run()

