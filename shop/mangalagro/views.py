import razorpay
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist, Feedback, Complaint
from .form import CustomerRegistrationForm, CustomerProfileForm, Feedbackform, Complaintform


RAZOR_KEY_ID = "rzp_test_5EhzoCUZIAMwWE"
RAZOR_KEY_SECRATE = "OpHNGwDrLSEYumGh6sG2YiYf"


# Create your views here.
@login_required
def index(request):
    totalitem = 0
    wishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
    product=Product.objects.all()
    user=request.user
    return render(request, 'home.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'register.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "congratulations ! user register successfully")
        else:
            messages.error(request, 'invalid Input data')



        return render(request, 'login.html', locals())


@login_required
def About(request):
    totalitem = 0
    wishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'about.html', locals())


@login_required
def Contect(request):
    totalitem = 0
    wishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'contact.html', locals())


@method_decorator(login_required, name='dispatch')
class Category(View):
    def get(self, request, val):
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        name = Product.objects.filter(category=val).values('name').annotate(total=Count('name'))
        return render(request, 'category.html', locals())


@method_decorator(login_required, name='dispatch')
class Categoryname(View):
    def get(self, request, val):
        product = Product.objects.filter(name=val)
        name = Product.objects.filter(category=product[0].category).values('name')
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'category.html', locals())


@method_decorator(login_required, name='dispatch')
class Productdetails(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'product_detail.html', locals())


@method_decorator(login_required, name='dispatch')
class Profile_view(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zip_code']
            reg = Customer(user=user, name=name, mobile=mobile, state=state, address=address, city=city,
                           zip_code=zipcode)
            reg.save()
            messages.success(request, "congratulations! user register successfully")
        else:
            messages.warning(request, 'invalid Input data')

        return render(request, 'profile.html', locals())


@login_required
def Address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'address.html', locals())


@method_decorator(login_required, name='dispatch')
class Updateaddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'updateaddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.city = form.cleaned_data['city']
            add.address = form.cleaned_data['address']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zip_code']
            add.save()
            messages.success(request, "congratulations! user register successfully")
        else:
            messages.warning(request, 'invalid Input data')

        return redirect('address')


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    print(product_id)
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")


def showcart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.price
        amount = amount + value
    totalamount = amount + 40
    totalitem = 0
    wishlist=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'addtocart.html', locals())


def show_wishlist(request):
    user=request.user
    totalitem = 0
    wishlist=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
    product=Wishlist.objects.filter(user=user)
    return render(request,'show_wishlist.html',locals())


@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        totalitem = 0
        wishlist = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishlist = len(Wishlist.objects.filter(user=request.user))
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.price
            famount = famount + value
        totalamount = famount + 40
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRATE))
        data = {"amount": razoramount, "currency": "INR"}
        payment_response = client.order.create(data=data)
        # print(payment_response)
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()
        return render(request, 'checkout.html', locals())


@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    print(cust_id)
    user = request.user
    customer = Customer.objects.get(id=cust_id)
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
    return redirect('orders')


@login_required
def orders(request):
    totalitem = 0
    wishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
    order_placed=[]
    order_placed = OrderPlaced.objects.filter(user=request.user)
    user=request.user
    order_placed = OrderPlaced.get_order_by_customer(user)
    print(order_placed, totalitem)
    return render(request, 'orders.html', locals())

@method_decorator(login_required, name='dispatch')
class feedback(View):
    def get(self, request,pk):
        form = Feedbackform(request.GET)
        order = OrderPlaced.objects.get(pk=pk)
        return render(request, 'feedback.html', locals())
    def post(self, request,pk):
        form = Feedbackform(request.POST)
        order = OrderPlaced.objects.get(pk=pk)
        if form.is_valid():
            description = form.cleaned_data['description']
            feed = Feedback(order=order, description=description)
            feed.save()
            return redirect('orders')

@method_decorator(login_required, name='dispatch')
class complaint(View):
    def get(self, request,pk):
        form = Complaintform(request.GET)
        order = OrderPlaced.objects.get(pk=pk)
        return render(request, 'complaint.html', locals())
    def post(self, request,pk):
        form = Complaintform(request.POST)
        order = OrderPlaced.objects.get(pk=pk)
        if form.is_valid():
            description = form.cleaned_data['description']
            feed = Complaint(order=order, description=description)
            feed.save()
            return redirect('orders')

@login_required
def bill(request,pk):
    order = OrderPlaced.objects.get(pk=pk)
    return render(request, 'bill.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']

        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount = amount + value
        totalamount = amount + 40

        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


def plus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        print(prod_id)
        product = Product.objects.get(id=prod_id)
        user = request.user
        print(user, product)
        Wishlist(user=user, product=product).save()
        data = {
            'massage': 'Wishlist Added Successfully',
        }
        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'massage': 'Wishlist Remove Successfully',
        }
        return JsonResponse(data)


def search(request):
    query = request.GET['search']
    totalitem = 0
    wishlist = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishlist = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(Q(name__icontains=query))
        return render(request, 'search.html', locals())


