from django.db import models
from django.contrib.auth.models import User
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