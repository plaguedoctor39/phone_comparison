from django.db import models


# Create your models here.
class Phone(models.Model):
    model_name = models.TextField()
    price = models.IntegerField()
    op_sys = models.TextField()
    ram = models.IntegerField()
    pixels_per_inch = models.IntegerField()
    double_cam = models.BooleanField(blank=True)
    processor = models.TextField()
    resolution = models.TextField()
    fm_radio = models.BooleanField(blank=True)

    class Meta:
        db_table = 'phones'


class ApplePhone(models.Model):
    add_info = ['Airpods', 'FaceId', 'ApplePay']


class SamsungPhone(models.Model):
    add_info = ['Двуторонний экран']
