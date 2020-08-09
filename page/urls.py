from django.contrib import admin
from django.urls import path, include
from .views
urlpatterns = [
    path('', views.cover, name="cover") # Cover 처음 페이지
]