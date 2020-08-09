from django.shortcuts import render
from page.models import Chicken

def cover(request):
    return render(request, 'cover.html')

def order(request):
    return render(request, 'order.html')