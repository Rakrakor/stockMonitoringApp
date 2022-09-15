
from django.urls import path, include
from . import views
#TODO:  "from . import" => it means from the current directory, import ...

# Management of the API #####
from rest_framework import routers
router = routers.DefaultRouter()
router.register('StockListAPI', views.StockView)
#############################

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html',views.about, name="about"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('add_stock.html/<stock_id>', views.home, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path ('', include(router.urls))
]