import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICE=(
    ('s','seeds'),
    ('f','fertilizer'),
    ('op','organic_Product'),
    ('p','pesticide'),
    ('ft','farm_tools'),
    ('i','irrigation'),
    ('b','bulk'),
    ('af','animalfood')
)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='upload/products/')

    def __str__(self):
        return self.name



class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    mobile=models.IntegerField(default='')
    state=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    zip_code=models.IntegerField()

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity *self.product.price

STATUS_CHOICE={
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Out of Delivery', 'Out of Delivery'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
}
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    ordered_date=models.DateTimeField(default=datetime.datetime.today)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE ,default="Pending")
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")

    def __str__(self):
            return str(self.id)

    @staticmethod
    def get_order_by_customer(user_id):
        return OrderPlaced.objects.filter(user=user_id).order_by('-ordered_date')
    @property
    def total_cost(self):
        return self.quantity *self.product.price


class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)





class Feedback(models.Model):
    order=models.ForeignKey(OrderPlaced,on_delete=models.CASCADE)
    description=models.CharField(max_length=5000)
    date=models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return str(self.id)

class Complaint(models.Model):
    order=models.ForeignKey(OrderPlaced,on_delete=models.CASCADE)
    description=models.CharField(max_length=5000)
    date=models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return str(self.id)