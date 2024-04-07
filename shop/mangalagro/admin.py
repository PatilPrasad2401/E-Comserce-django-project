from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin.register(Product)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']

@admin.register(Customer)
class CustomrModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','user','city','state','zip_code','mobile']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']



@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status','payment']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','order','description','date']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id','order','description','date']
