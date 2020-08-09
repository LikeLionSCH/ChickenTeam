from django.shortcuts import render
from page.models import Chicken

def cover(request):
    return render(request, 'cover.html')