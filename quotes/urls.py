
from django.urls import path
from . import views
#TODO:  "from . import" => it means from the current directory, import ...

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html',views.about, name="about"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('add_stock.html/<stock_id>', views.home, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
]