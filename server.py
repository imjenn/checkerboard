from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display():
    return render_template("index.html", x=8, y=8)

@app.route('/<int:row>')
def display4(row):
    return render_template("index.html", x=row, y=8)

@app.route('/<int:row>/<int:col>')
def displayMany(row, col):
    return render_template("index.html", x=row, y=col)

@app.route('/<int:row>/<int:col>/<string:color1>')
def displayColor(row, col, color1):
    return render_template("index.html", x=row, y=col, color1=color1)

@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def displayManyColors(row, col, color1, color2):
    return render_template("index.html", x=row, y=col, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)