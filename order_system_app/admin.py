from django.contrib import admin

# Register your models here.
# After creating models for a table in database, it will not be showned until we register it in admin.py

from order_system_app.models import Restaurant

admin.site.register(Restaurant)
