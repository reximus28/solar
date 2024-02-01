from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SolarPanel(models.Model):
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    capacity = models.FloatField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='solar_panels')

    def __str__(self):
        return f"{self.brand} {self.model}"

class SolarInverter(models.Model):
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    capacity = models.FloatField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='inverters')

    def __str__(self):
        return f"{self.brand} {self.model}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    panels_ordered = models.ManyToManyField(SolarPanel, related_name='orders')
    inverters_ordered = models.ManyToManyField(SolarInverter, related_name='orders')
    order_date = models.DateField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"Order for {self.customer} on {self.order_date}"
