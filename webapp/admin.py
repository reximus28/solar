from django.contrib import admin
from .models import Customer, ProductCategory, SolarPanel, SolarInverter, Order

admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(SolarPanel)
admin.site.register(SolarInverter)
admin.site.register(Order)