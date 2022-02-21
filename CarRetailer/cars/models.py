from django.db import models

class car(models.Model):
    brand_name = models.CharField(default="")
    model_name = models.CharField(default="")
    year = models.IntegerField(default=2000)
    mileage = models.IntegerField(defualt=10000)
