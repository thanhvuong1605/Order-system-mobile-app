## create file for API !
from rest_framework import serializers

from order_system_app.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    def get_logo(self,restaurant):          #this function for displaying the url of logo, which
        request = self.context.get('request')   #include also the domain not just the path
        logo_url = restaurant.logo.url

        return request.build_absolute_uri(logo_url)

    class Meta:
        model =Restaurant
        fields = ("id","name","phone","address","logo")
