from django.http import JsonResponse
from order_system_app.models import Restaurant,Meals ,Order , OrderDetails
from order_system_app.serializers import RestaurantSerializer,MealsSerializer,OrderSerializer
import json
from oauth2_provider.models import AccessToken
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import stripe
from ordersystem.settings import STRIPE_API_KEY
stripe.api_key = STRIPE_API_KEY

def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("id"),
        many=True,
        context = {"request": request}
    ).data

    return JsonResponse({"restaurants":restaurants})


def customer_get_meals(request,restaurant_id):   #restaurant_id from the url
    meals = MealsSerializer(
        Meals.objects.filter(restaurant_id = restaurant_id).order_by("id"),
        many=True,
        context = {"request": request}
    ).data
    return JsonResponse({"meals":meals})


@csrf_exempt
def customer_add_order(request):
    """
        De tao cai order nay can nhung params giong luc test tren POSTMAN
            access_token
            restaurant_id
            address
            order_details
            stripe_token for payment

            status


        Cai nao ma can dung request.POST thi` se~ khai bao' o? POSTMAN
    """
    if request.method == "POST":
        #get access_token
        access_token = AccessToken.objects.get(token = request.POST.get("access_token"),
            expires__gt = timezone.now())

        #get profile
        customer = access_token.user.customer


        #get stripe token
        stripe_token =request.POST["stripe_token"]

        #check address, but not necessary, if user doesnt give address ~> it means it will be picked up
        # if not request.POST["address"]:
        #     return JsonResponse({"status":"failed","error":"Address is required"})

        #get order detail
        order_details = json.loads(request.POST["order_details"])

        order_total = 0
        for meal in order_details:
            order_total = Meals.objects.get(id = meal["meal_id"]).price*meal["quantity"]

        if len(order_details) > 0:

            #Create a charge: this will charge customer card
            charge = stripe.Charge.create(
                amount = order_total * 100, #amount in cents
                currency = "EUR",
                source = stripe_token,
                description = "Order system"
            )
            if charge.status != "failed":

                #create an order
                order = Order.objects.create(
                    customer = customer,
                    restaurant_id = request.POST["restaurant_id"],
                    total = order_total,
                    status= Order.COOKING,
                    address = request.POST["address"]
                )

                    #create order detail
                for meal in order_details:
                    OrderDetails.objects.create(
                        order = order,
                        meal_id = meal["meal_id"],
                        quantity = meal["quantity"],
                        sub_total = Meals.objects.get(id = meal["meal_id"]).price*meal["quantity"]
                    )

                return JsonResponse({"status":"success"})
            else:
                return JsonResponse({"status":"failed","error":"Could not complete payment."})


def customer_get_latest_order(request):
    access_token = AccessToken.objects.get(token = request.GET.get("access_token"),
        expires__gt = timezone.now())
    customer = access_token.user.customer
    order = OrderSerializer(Order.objects.filter(customer = customer).last()).data


    return JsonResponse({"order":order})


# def restaurant_order_noti(request,last_request_time):
#     noti = Order.objects.filter(restaurant = request.user.restaurant, created_at__gt = last_request_time).count()
#
#     #as SQL language select count(*) from Orders where restaurant = request.user.restaurant AND create_at > last_request_time
#
#     return JsonResponse({"noti":noti})
