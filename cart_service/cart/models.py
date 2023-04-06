from django.db import models

# Create your models here.
class Item(models.Model):
    product_id = models.CharField(max_length=128, primary_key= True)
    quantity = models.CharField(max_length=128)

    def __str__(self):
        return self.product_id

class Cart(models.Model):
    username = models.CharField(max_length=128)
    cart = models.ManyToManyField(Item, through='Membership')

    def __str__(self):
        return self.username

class Membership(models.Model):
    person = models.ForeignKey(Item, on_delete=models.CASCADE)
    group = models.ForeignKey(Cart, on_delete=models.CASCADE)