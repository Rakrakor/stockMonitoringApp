
#TODO: 1) TERMINAL : create an app
#TODO: 2) in settings.py, When an app is created, list the app into the settings.py file
#TODO: 3) in url.py, add the path to the newly created app. add the include import of this main urls.py file
#TODO: 4) in the created app folder, create a templates folder
#TODO: 5) in the template folder, create the html files(views) that will be displayed
#TODO 6) in views.py Create a function to render a specific html file
#TODO 7) in url.py include the views file into the urls.py file
#TODO 8) in url.py  linked the url path, to the views function that renders a html file: URL <=> view.function: return file.html
#TODO 9) in app folder  create a base template . Incorporate the tempate to all the html files
#TODO 10) Go to bootstrap and copy the starter template to the base.py. Move the {blocks content} into the <body>
#TODO 11) Convert all the link as following :href="{% url 'about' %}". They are a reference to the URL.py links
#TODO 12) In order to pull out data from the market, Log in the stock market API called : https://iexcloud.io/cloud-login#/register/
#TODO 13) go to the home page and get the PUBLIC API KEY: pk_f3cf7858163e4525b467452e90fd8df2
#TODO 13) and sk_c4acbb380f424241b8e01589bf9edcfc
#TODO 14) To understand how to call the API read: https://iexcloud.io/docs/api/#data-points
#TODO 15) views.py : import requests and import json. (Json comes with python.But do pip install requests).
#TODO 16) select which data will be displayed via in the base.html
#TODO 17) avoid hackers : in the base.html in the under the search bar form section add : {% csrf_token %}
#TODO 18) in the base.html change the search to QUote Search
#TODO 19) in the base.html add this to the Quote Search form:  action="{% url 'home' %}" method=""POST
#TODO 20) in the base.html add this to the form input field: name="ticker"
#TODO 21) in the views.py add the POST method check condition
#TODO 21) in the views.py if the POST conditions are not met, return and render a new string indicating the error
#TODO 21) in the home.html destructure the new string variable
#TODO 22) in the views.py get the ticker Name from the POST list
#TODO 23) in the views.py concatenate ticker to the API url access
#TODO 24) in models.py ( Database table ) Create a Class Stock
#TODO 25) in the terminal makemigration / migrate
#TODO 26) in admin.py register the newly create class, so it is visible in the admin
#TODO 27) in the admin section add a few stocks in the DB
#TODO 28) create the add_stock.html ( i.e add the render function in the views.py / loop through the Items in DB)
#TODO 29) Create a StockForm ( other way to use form but with Django framwork)
#TODO 30) in the view.py Create a new function delete()
#TODO 31) from the add_stock.html create a link to call the URL path delete with parameter < ID >

# CREATE API
#TODO: 32-Create a SERIALIZER ( see www.django-rest-framework.org)
#TODO: 33-  (it will transform the data into JSON )
#TODO: 34-  Create a new file: serializers.py
#TODO: 35-  import the serializers package , AND the MODELS we want to serialize
#TODO: 36-  define a class that extends ModelSerializer
#TODO: 37-  Define a sub class Meta: with paramaters Models, fields

#TODO: 38-Create VIEW: create a CLASS (not a fonction) in the views.py, that handles the dataset <=> the serializer Class
#TODO: 39-  the class extends 'viewsets.ModelViewSet',  from rest_framework import viewsets
#TODO: 40-  the 2 new parameters are: queryset=Stock.objects.all() and serializer_class = StockSerializer

#TODO: 41-Create the URL:
#TODO: 42-  import and use router = routers.DefaultRouter()
#TODO: 43-  register the 2 parameters: 'desired URI', StockView function from views.py
#TODO: 44-  in the path, include the router : path('', include(router.urls)




