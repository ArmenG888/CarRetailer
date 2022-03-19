from django.db import models

class brand(models.Model):
    brand_name = models.CharField(max_length=50,default='')
    slug = models.SlugField(default="")
    brand_logo = models.ImageField(upload_to='brand_logos',blank=True)

    def __str__(self):
        return self.brand_name

class car_model(models.Model):
    brand = models.ForeignKey(brand,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50,default='')
    mileage = models.IntegerField(default=0)
    damaged = models.BooleanField(default=False)
    image = models.ImageField(upload_to="car_images",blank=True)

    def __str__(self):
        return self.model_name