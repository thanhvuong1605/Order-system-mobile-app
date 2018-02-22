from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from order_system_app.forms import UserForm, RestaurantForm, UserFormEdit,MealsForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from order_system_app.models import Meals
# Create your views here.

def home(request):
    return redirect(restaurant_home)



#restaurant part
@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/order.html',{})




@login_required(login_url='/restaurant/sign-in/')
def restaurant_account(request):
    user_form = UserFormEdit(instance = request.user)
    restaurant_form =RestaurantForm(instance =request.user.restaurant)

    if request.method == 'POST':
        user_form = UserFormEdit(request.POST, instance = request.user)
        restaurant_form =RestaurantForm(request.POST,request.FILES, instance = request.user.restaurant)

        if user_form.is_valid() and restaurant_form.is_valid():
            user_form.save()
            restaurant_form.save()


    return render(request, 'restaurant/account.html',{
    "user_form": user_form,
    "restaurant_form": restaurant_form
    })


@login_required(login_url='/restaurant/sign-in/')
def restaurant_meals(request):
    meals = Meals.objects.filter(restaurant = request.user.restaurant).order_by("id") #-id to revert order
    return render(request, 'restaurant/meals.html',{"meals":meals})
#to display list of meal on meal page




@login_required(login_url='/restaurant/sign-in/')
def restaurant_add_meals(request):
    meals_form = MealsForm()

    if request.method == "POST":
        meals_form = MealsForm(request.POST,request.FILES)
        if meals_form.is_valid:
            meals = meals_form.save(commit=False)
            meals.restaurant = request.user.restaurant
            meals.save()
            return redirect(restaurant_meals)

    return render(request, 'restaurant/add_meals.html',{
    "meals_form" : meals_form
    })


@login_required(login_url='/restaurant/sign-in/')
def restaurant_edit_meals(request,meal_id):
    meals_form = MealsForm(instance=Meals.objects.get(id=meal_id)) # edit the meal based on id

    if request.method == "POST":
        meals_form = MealsForm(request.POST,request.FILES,instance=Meals.objects.get(id=meal_id))
        if meals_form.is_valid:
            meals_form.save()
            return redirect(restaurant_meals)

    return render(request, 'restaurant/edit_meals.html',{
    "meals_form" : meals_form
    })



@login_required(login_url='/restaurant/sign-in/')
def restaurant_order(request):
    return render(request, 'restaurant/order.html',{})





@login_required(login_url='/restaurant/sign-in/')
def restaurant_report(request):
    return render(request, 'restaurant/report.html',{})






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
