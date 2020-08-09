from django.contrib import admin
from django.urls import path, include
from .views import cover, order
urlpatterns = [
    path('', cover, name="cover"), # Cover 처음 페이지
    path('order/', order, name="order") # Order 페이지 - 메뉴주문 메인 페이지
]