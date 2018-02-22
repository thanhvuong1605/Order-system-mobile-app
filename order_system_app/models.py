from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name = 'restaurant')
    #one to one, restaurant belong to one owner, one user has only 1 restaurent. on_delete is when
    #deleting the user, the restaurant will be deleted too!!!
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to = 'restaurant_logo/',blank=False)
    #imageField needs the Pillow package!

    def __str__(self):
        return self.name #this str method for displaying the name of restaurant on database with nice str, by default it returns id

# whenever updating or creating a models, need to make migration again!


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Meals(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'meals_images/',blank=False)
    price = models.IntegerField(default = 0)

    def __str__(self):
        return self.name


class Order(models.Model):
    COOKING = "Cooking"
    READY ="Ready"
    ONTHEWAY ="On the way"
    DELIVERED="Delivered"

    STATUS_CHOICE = {
        (COOKING,"Cooking"),
        (READY,"Ready"),
        (ONTHEWAY,"On the way"),
        (DELIVERED, "Delivered"),
    }

    customer = models.ForeignKey(Customer)
    restaurant = models.ForeignKey(Restaurant)
    address = models.CharField(max_length=500)
    total = models.FloatField()
    status = models.CharField(choices =STATUS_CHOICE,max_length=500)
    created_at = models.DateTimeField(default = timezone.now)
    picked_at = models.DateTimeField(blank=True,null = True)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order,related_name='order_details')
    meal = models.ForeignKey(Meals)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)
