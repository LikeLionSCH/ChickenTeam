from django.contrib import admin
from django.urls import path, include
from .views import cover, order, about
urlpatterns = [
    path('', cover, name="cover"), # Cover 처음 페이지
    path('order/', order, name="order"), # Order 페이지 - 메뉴주문 메인 페이지
    path('about/', about, name="about"), # About 페이지 - 페이지 설명 페이지
]