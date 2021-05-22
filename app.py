from flask import Flask,render_template,request
import requests

api_key = #Your Fixer API key should be on there like a string value 
url = "http://data.fixer.io/api/latest?access_key="+api_key

# made by me github desktop

app = Flask(__name__)

@app.route("/" , methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") # EURO
        secondCurrency = request.form.get("secondCurrency") # TRY
        amount = request.form.get("amount") #20
        response = requests.get(url)
        #app.logger.info(response)
        infos = response.json()
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]
        result = (secondValue / firstValue) * float(amount)
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        #app.logger.info(infos)
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")









if __name__ == "__main__":
    app.run(debug = True)
