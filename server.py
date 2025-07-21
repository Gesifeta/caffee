from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
caffes =[]
with open("cafe-data.csv", "r",encoding="utf-8") as csvfile:
    caffes = csvfile.readlines()

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/cafes')
def cafes():
    return render_template("cafes.html",cafes=caffes)
if __name__ == '__main__':
    app.run(debug=True)