## create file for API !
from rest_framework import serializers

from order_system_app.models import Restaurant,Meals, Customer, Order,OrderDetails

class RestaurantSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    def get_logo(self,restaurant):          #this function for displaying the url of logo, which
        request = self.context.get('request')   #include also the domain not just the path
        logo_url = restaurant.logo.url

        return request.build_absolute_uri(logo_url)

    class Meta:
        model =Restaurant
        fields = ("id","name","phone","address","logo")


class MealsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self,meals):          #this function for displaying the url of logo, which
        request = self.context.get('request')   #include also the domain not just the path
        image_url = meals.image.url

        return request.build_absolute_uri(image_url)

    class Meta:
        model = Meals
        fields = ("id","name","description","image","price")



## ORDER SERIALIZER, need to transfer info from the database to json and pass it to the customer
## need to create so many Serializer to create JSON for each variable and pass it to OrderSerializer
## otherwise it wont work
class OrderCustomerSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source = "user.get_full_name")

    class Meta:
        model = Customer
        fields = ("id","name","avatar","phone","address")


class OrderRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ("id","name","phone","address")


class OrderMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ("id","name","price")

class OrderDetailsSerializer(serializers.ModelSerializer):
    meals = OrderMealsSerializer
    class Meta:
        model = OrderDetails
        fields = ("id","meal","quantity","sub_total")

class OrderSerializer(serializers.ModelSerializer):
    customer = OrderCustomerSerializer()
    restaurant = OrderRestaurantSerializer()
    order_details = OrderDetailsSerializer(many = True)
    status = serializers.ReadOnlyField(source="get_status_display")

    class Meta:
        model = Order
        fields= ("id","customer","restaurant","order_details","total","status","address")
