from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    true_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    sex = models.SmallIntegerField()
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name='文件缩略图', blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=30, null=True)
    is_delete = models.SmallIntegerField(blank=True, null=True)
    creater = models.CharField(max_length=32)
    create_date = models.DateTimeField()
    updater = models.CharField(max_length=32, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
