from django.db import models

class brand(models.Model):
    brand_name = models.CharField(max_length=50,default='')
    slug = models.SlugField(default="")
    brand_logo = models.ImageField(upload_to='brand_logos',blank=True)
    cars_to_brand = models.ManyToManyField("cars.car_model",blank=True)
    def __str__(self):
        return self.brand_name
    
class car_model(models.Model):
    manufacture = models.ForeignKey(brand,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50,default='')
    mileage = models.IntegerField(default=0)
    price = models.IntegerField(default=1000)
    damaged = models.BooleanField(default=False)
    image = models.ImageField(upload_to="car_images",blank=True)
    viewed = models.IntegerField(default=0)
    def __str__(self):
        return self.model_name