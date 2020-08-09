from django.contrib import admin
# Register your models here.
from .models import Chicken

admin.site.register(Chicken) # 어드민 계정에서 사용