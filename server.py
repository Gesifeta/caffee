
from flask import Flask, render_template,request
import pandas as pd
app = Flask(__name__)
caffes =[]

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/cafes')
def cafes():
    with open("cafe-data.csv", "r", encoding="utf-8") as csvfile:
        caffes = csvfile.readlines()

    return render_template("cafes.html",cafes=caffes)


@app.route('/cafes/add')
def new_cafe_form():
    return render_template("new_cafe_form.html")


@app.route('/cafes/add', methods=['POST'])
def add_cafe():
    data = request.form
    cafe_data={
        "Name": data["cafe_name"],
        "Location": data["location"],
        "open": data["open"],
        "close": data["close"],
        "coffee": data["coffee_rating"],
        "wifi": data["wifi_rating"],
        "power": data["power_availability"]
    }

    with open("cafe-data.csv", "a",encoding="utf-8") as csvfile:
        new_data =''
        for item in cafe_data.keys():
            new_data += cafe_data[item] + ","
        csvfile.write("\n"+new_data[:len(new_data)-1])
    return "success"

if __name__ == '__main__':
    app.run(debug=True)