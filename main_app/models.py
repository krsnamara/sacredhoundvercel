from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Item(models.Model):
    name = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.id})

class Cart(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cart_id': self.id})
    
# class CartItem(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f'{self.quantity} x {self.item}'