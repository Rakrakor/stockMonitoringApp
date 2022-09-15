from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from os import strerror

import requests
import json

apiGetRequestVAR ={"api_request":0, "apiJSON":1}

def APIGetRequest(ticker):
    api_request = requests.get(
        "https://cloud.iexapis.com/stable/stock/" + str(ticker) + "/quote?token=sk_c4acbb380f424241b8e01589bf9edcfc")
    api = json.loads(api_request.content)
    return (api_request, api)

def home(request, stock_id=None):

    if request.method == 'POST':
        #Ticker is the variable name given to the input field of the search bar in the base.html
        ticker = request.POST['ticker']
        try:
            APIGetResult = APIGetRequest(ticker)
            api_request = APIGetResult[apiGetRequestVAR["api_request"]]
            api = APIGetResult[apiGetRequestVAR["apiJSON"]]
        except Exception as e:
            api = "BigError"
            print(e)
        return render(request, 'home.html', {'api': api, 'stock':ticker, 'request_status': api_request.status_code})
    else:
        if stock_id is None:
            stock = 'VANTAGE:SP500'
        else:
            stock = stock_id
        return render(request, 'home.html', {'ticker':'⬇️ Search a quote ⬇️', 'stock':stock})

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
            try:
                ticker_item = request.POST['ticker']
                APIGetResult = APIGetRequest(ticker_item) #function will propagates exception if not able to retrieve api result
                form.save()
                messages.success(request, ("Stock has been succesfully saved !"))
            except Exception as e:
                messages.warning(request, ("This ticker does not exist"))
                print(e)

            return redirect('add_stock')

    else:

        tickerInDb = Stock.objects.all()
        output=[]
        for ticker_item in tickerInDb:
            try:

                APIGetResult = APIGetRequest(ticker_item)
                api = APIGetResult[apiGetRequestVAR["apiJSON"]]
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


from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer