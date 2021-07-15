import csv
from flask import Flask
from flask import request, redirect
from flask import render_template

data = {}
with open("bank_quest_simple.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvreader:
        data[row[1]]=row[2]

app = Flask(__name__)

@app.route("/currency/calc", methods=["GET", "POST"])
def calculator():
    if request.method=="GET":
        return render_template("calc.html")
    elif request.method=="POST":
        cur=request.form.get("cur")
        quant=float(request.form.get('quant'))

        val=float(data.get(cur))

        cost = val * quant

        return render_template("calc_result.html", cost=cost)
        

if __name__ == "__main__":
    app.run(debug=False)
