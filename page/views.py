from django.shortcuts import render
from page.models import Chicken

def cover(request): # cover 페이지
    return render(request, 'cover.html')

def order(request):
    chickens = Chicken.objects.all() # order main 페이지에 현재 치킨 메뉴 정하기
    return render(request, 'order.html', {'chickens':chickens})

def about(request): # about 페이지 이동
    return render(request, 'about.html')

def contain(request):
    return redirect('order')

# def delete(request, chicken_id):
#     return redirect()