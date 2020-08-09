from django.contrib import admin
from django.urls import path, include
from .views import cover, order, about, finish, cart
urlpatterns = [
    path('', cover, name="cover"), # Cover 처음 페이지
    path('order/', order, name="order"), # Order 페이지 - 메뉴주문 메인 페이지
    path('about/', about, name="about"), # About 페이지 - 페이지 설명 페이지
    path('finish/', finish, name="finish"), # Finish 페이지 - 주문 완료 후 order로 돌아가는 페이지
    path('cart/', cart, name="cart"), # Cart 페이지 - order 페이지에서 장바구니에 추가 한 값 보여주기
]