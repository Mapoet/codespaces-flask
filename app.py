from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/data")
def data_page():
    return "你已经打开了一个新的数据页"
