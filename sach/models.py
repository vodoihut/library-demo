from django.db import models

# Create your models here.

class danhmuc(models.Model):
    ten = models.CharField(default='',  max_length=100)
    duongdan = models.CharField(max_length=100, default='')
    mota = models.TextField(default='')
    hoatdong = models.BooleanField(default=True)


class sach(models.Model):
    ten = models.CharField(max_length=255, default='')
    mota = models.TextField(default='')
    danhmuc = models.ForeignKey(danhmuc, on_delete=models.CASCADE)
    book_img = models.CharField(max_length=255, default='')
    hoatdong = models.BooleanField(default=True)