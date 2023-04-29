from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tax_rate = 0.15

def index(request):
    return HttpResponse("this is a site to calculate tax!")

def taxCalc(request,price):
    price = int(price)
    finalPrice = (price * tax_rate) + price
    return HttpResponse(f"The total price after 15% tax is: {finalPrice}")

def taxRate(request):
    return HttpResponse(f"<h1> {tax_rate*100}% </h1>")