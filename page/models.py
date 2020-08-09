from django.db import models

# Create your models here.
class Chicken(models.Model):
    image = models.ImageField(upload_to = 'images/') # 치킨이미지
    name = models.CharField(max_length=50) # 치킨이름
    money = models.IntegerField() # 치킨가격
    description = models.TextField() # 치킨설명
