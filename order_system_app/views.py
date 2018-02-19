from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from order_system_app.forms import UserForm, RestaurantForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return redirect(restaurant_home)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html',{})


def restaurant_sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    #after user click sign up button, run these function:
    if request.method == "POST":

        #get data from forms
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST,request.FILES)

        #check if information is valid
        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)  #create new user object
            new_restaurant = restaurant_form.save(commit=False)           #create new restaurant, just memory not data yet
            new_restaurant.user = new_user                                #asgin user to restaurant
            new_restaurant.save()                                         #save to database

            login(request,authenticate(
                username = user_form.cleaned_data["username"],        #login
                password = user_form.cleaned_data["password"]
            ))

            return redirect(restaurant_home)



    return render(request, 'restaurant/sign_up.html',{
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })
