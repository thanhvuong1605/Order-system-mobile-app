from django.http import JsonResponse

from order_system_app.models import Restaurant
from order_system_app.serializers import RestaurantSerializer

def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("id"),
        many=True,
        context = {"request": request}
    ).data

    return JsonResponse({"restaurants":restaurants})
