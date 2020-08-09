from django.shortcuts import render
from page.models import Chicken

def cover(request):
    return render(request, 'cover.html')

def order(request):
    chickens = Chicken.objects.all()
    return render(request, 'order.html', {'chickens':chickens})

def about(request):
    return render(request, 'about.html')

# def delete(request, chicken_id):
#     return redirect()