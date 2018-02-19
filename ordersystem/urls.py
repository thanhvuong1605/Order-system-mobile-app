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
from django.conf.urls import url
from django.contrib import admin
from order_system_app import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^restaurant/sign-in/$',auth_views.login, {'template_name':'restaurant/sign_in.html'},name='restaurant-sign-in'),
    url(r'^restaurant/sign-out/$',auth_views.logout,{'next_page':"/"},name='restaurant-sign-out'),
    #Sign in takes the function named login in views.py and redirect the page to sign_in.html which called restaurant-sign-in
    #for sigining out it goes to the home page so it has only /
    #name of url for calling it in put in <a> tag, example <a href = url 'restaurant-sign-out'
    url(r'^restaurant/sign-up/$',views.restaurant_sign_up,name='restaurant-sign-up'),
    url(r'^restaurant/$', views.restaurant_home,name='restaurant-home')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#for uploading the images need to use static 
