from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from os import strerror


def home(request):

    import requests
    import json

    if request.method == 'POST':
        #Ticker is the variable name given to the input field of the search bar in the base.html
        ticker = request.POST['ticker']
        try:
            api_request = requests.get(
                "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=sk_c4acbb380f424241b8e01589bf9edcfc")
            api = json.loads(api_request.content)
        except Exception as e:
            api = "BigError"
            print(e)
        return render(request, 'home.html', {'api': api, 'stock':ticker, 'request_status': api_request.status_code})
    else:
        return render(request, 'home.html', {'ticker':'⬇️ Search a quote ⬇️', 'stock':'VANTAGE:SP500'})

    #api_request = requests.get("https://cloud.iexapis.com/stable/stock/appl/quote?token=pk_f3cf7858163e4525b467452e90fd8df2")
    #api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=sk_c4acbb380f424241b8e01589bf9edcfc")
    #api_request = requests.get("https://cloud.iexapis.com/v1/sql-query/STOCKSAPP?token=sk_c4acbb380f424241b8e01589bf9edcfc&sqlQuery=SELECT%20*%20FROM%20CORE.%60COMPANY%60%20LIMIT%2010")

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})

from .models import Stock
from django.contrib import messages
from .forms import StockForm
def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been succesfully saved !"))
            return redirect('add_stock')

    else:

        tickerInDb = Stock.objects.all()
        output=[]
        for ticker_item in tickerInDb:
            try:
                api_request = requests.get(
                    "https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=sk_c4acbb380f424241b8e01589bf9edcfc")
                api = json.loads(api_request.content)
                output.append((ticker_item.id, api))
            except Exception as e:
                api = "BigError"
                print(e)

        return render(request,'add_stock.html', {'tickerInDb':tickerInDb, 'output':output })


def delete(request, stock_id):
    item =Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock successfully deleted"))
    return redirect (add_stock)