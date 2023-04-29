from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name = "index"),
    path("taxrate",views.taxRate,name = "Calculater"),
    path("<str:price>",views.taxCalc,name = "Calculater"),
    
]