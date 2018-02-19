from django import forms
from django.contrib.auth.models import User
from order_system_app.models import Restaurant


# the modelform for registering, so information of user and restaurant go straigh to the database
class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required = True)
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username","password","first_name","last_name","email")

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name","phone","address","logo")
