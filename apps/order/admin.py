from django.contrib import admin

# Register your models here.

from .models import Order, OrdenItem

admin.site.register(Order)
admin.site.register(OrdenItem)