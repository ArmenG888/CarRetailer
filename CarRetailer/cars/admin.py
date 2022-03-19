from django.contrib import admin
from .models import brand,car_model


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand_name",)}

admin.site.register(brand,BrandAdmin)
admin.site.register(car_model)
