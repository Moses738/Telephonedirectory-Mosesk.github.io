from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
dict={}
@app.route("/add", methods=["GET","POST"])
def add():
    name= request.form.get("name")
    number = request.form.get("number")
    dict[name]=number
    return render_template("add.html", dict=dict, name = name, number = number)

@app.route("/display", methods=["GET","POST"])
def display():
    return render_template("display.html",dict=dict)

@app.route("/search", methods=["GET","POST"])
def search():
    name=request.form.get("name")
    return render_template("search.html",dict=dict, name=name)

if __name__ == '__main__':
    app.run(debug=True)
