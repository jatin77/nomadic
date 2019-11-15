from django.db import models
from guides.models import Guide

class Listing(models.Model):
    guide=models.ForeignKey(Guide,on_delete=models.DO_NOTHING)
    city=models.CharField(max_length=100,default='city')
    country=models.CharField(max_length=100,default='country')
    state=models.CharField(max_length=100,default='state')
    internet=models.CharField(max_length=100,default='internet')
    description=models.TextField(blank=True)
    nomad_cost=models.IntegerField(default=0)
    beer=models.IntegerField(default=0)
    coffee=models.IntegerField(default=0)
    population=models.IntegerField(default=0)
    male_ratio=models.IntegerField(default=0)
    female_ratio=models.IntegerField(default=0)
    cococola=models.IntegerField(default=0)
    free_wifi=models.CharField(max_length=100,default='wifi')
    english_speaking=models.CharField(max_length=100,default='language')
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/',default='img')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='img')
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='img')
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='img')
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='img')
    photo_5:models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='img')
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='img')
    def __str__(self):
        return self.city