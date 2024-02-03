from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    # Add more fields as required

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    # Additional fields like order status

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
