"""ordersystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from order_system_app import views,apis
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    #restaurant urls
    url(r'^restaurant/sign-in/$',auth_views.login, {'template_name':'restaurant/sign_in.html'},name='restaurant-sign-in'),
    url(r'^restaurant/sign-out/$',auth_views.logout,{'next_page':"/"},name='restaurant-sign-out'),
    #Sign in takes the function named login in views.py and redirect the page to sign_in.html which called restaurant-sign-in
    #for sigining out it goes to the home page so it has only /
    #name of url for calling it in put in <a> tag, example <a href = url 'restaurant-sign-out'
    url(r'^restaurant/sign-up/$',views.restaurant_sign_up,name='restaurant-sign-up'),
    url(r'^restaurant/$', views.restaurant_home,name='restaurant-home'),


    url(r'^restaurant/account/$', views.restaurant_account,name='restaurant-account'),
    url(r'^restaurant/meals/$', views.restaurant_meals,name='restaurant-meals'),
    url(r'^restaurant/meals/add$', views.restaurant_add_meals,name='restaurant-add-meals'),
    url(r'^restaurant/meals/edit/(?P<meal_id>\d+)/$', views.restaurant_edit_meals,name='restaurant-edit-meals'),
    url(r'^restaurant/order/$', views.restaurant_order,name='restaurant-order'),
    url(r'^restaurant/report/$', views.restaurant_report,name='restaurant-report'),

    #sign in sign out sign up blah blah with rest api
    url(r'^auth_fb/', include('rest_framework_social_oauth2.urls')),
    #/convert-token (sign in/sign up)
    #/revoke-token(sign-out)


    #api urls
    url(r'^api/customer/restaurants/$',apis.customer_get_restaurants),
    url(r'^api/customer/meals/(?P<restaurant_id>\d+)/$',apis.customer_get_meals), #\d is for number
    url(r'^api/customer/order/add/$',apis.customer_add_order),
    url(r'^api/customer/order/latest/$',apis.customer_get_latest_order),
        #api for order noti
    # url(r'^api/restaurant/order/noti/(?P<last_request_time>.+)/$', apis.restaurant_order_noti), #. for str
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#for uploading the images need to use static
