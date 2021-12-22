from django.contrib import admin
import datetime
from django.urls import reverse
from .models import Order, OrdenItem
from django.core.mail import send_mail
from django.template.loader import render_to_string

def order_name(obj):
    return '%s %s' % (obj.first_name,obj.last_name)
order_name.short_description = 'Name'

def admin_order_shipped(modeladmin,request,queryset):
    for order in queryset:
        order.shipped_date=datetime.datetime.now()
        order.status=Order.SHIPPED
        order.save()
        html=render_to_string('order_sent.html',{'order':order})
        send_mail('Order sent','Your Order has been sent!','noreply@shop.com',['mail@shop.com', order.email], fail_silently=False,html_message=html)
    return

class OrderItemInline(admin.TabularInline):
    model=OrdenItem
    raw_id_fields=['product']
class OrderAdmin(admin.ModelAdmin):
    list_display=['id',order_name,'created_at']
    list_filter=['created_at','status']
    search_fields=['first_name','address']
    inlines=[OrderItemInline]
    actions=[admin_order_shipped]
    
    
admin.site.register(Order,OrderAdmin)
admin.site.register(OrdenItem)