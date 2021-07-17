from django.db import models

# Create your models here.

class Info( models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField( max_length=120, primary_key = True)
    password = models.CharField( max_length=120)


# class Data( models.Model):
#     file_name = models.FileField(upload_to= 'datas')
#     uploaded = models.DateTimeField(auto_now_add=True)
#     activated = models.BooleanField(default=False)
#
#     def  __str__(self):
#         return  f"File id: {self.id}"










class Data( models.Model):

    model = models.CharField(max_length=120)
    make = models.CharField(max_length=120)
    Variant = models.CharField(max_length=120)
    price = models.FloatField(max_length=120)
    fuel_type = models.CharField(max_length=120)
    Link = models.CharField( max_length=2000)
    image_link = models.CharField( max_length=2000)