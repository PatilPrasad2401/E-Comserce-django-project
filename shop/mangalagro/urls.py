from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from .form import Loginform, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('',index),
    path('profile/', Profile_view.as_view(), name='profile'),

    path('address/', Address, name='address'),
    path('update_address/<int:pk>',Updateaddress.as_view(), name='update_address'),
    # path('delete_address/<int:pk>',delete_address, name='delete_address'),

    path('contact/',Contect,name='contact'),
    path('about/',About,name='about'),

    path('category/<slug:val>',Category.as_view(),name='category'),
    path('categoryname/<val>',Categoryname.as_view(),name='categoryname'),
    path('product_detail/<int:pk>',Productdetails.as_view(), name='product_detail'),

    path('orders/', orders, name='orders'),
    path('add-to-cart',add_to_cart,name='add-to-cart'),
    path('cart',showcart,name='showcart'),
    path('wishlist',show_wishlist,name='wishlist'),
    path('checkout',checkout.as_view(),name='checkout'),
    path('paymentdone',payment_done,name='paymentdone'),
    path('invoice',payment_done,name='invoice'),

    path('feedback/<int:pk>', feedback.as_view(), name='feedback'),
    path('complaint/<int:pk>', complaint.as_view(), name='complaint'),
    path('bill/<int:pk>', bill, name='bill'),

    path('search/',search,name='search'),
    # path('complaint/<int:pk>',Complaint,name='complaint'),
    # path('feedback/',Complaint.as_view(),name='feedback'),

    path('pluscart/',plus_cart),
    path('minuscart/',minus_cart),
    path('removecart/',remove_cart),
    path('pluswishlist/',plus_wishlist),
    path('minuswishlist/',minus_wishlist),

#     login Authenation
    path('register',CustomerRegistrationView.as_view(),name='CustomerRegistration'),
    path('accounts/login/', auth_view. LoginView.as_view(template_name='login.html',authentication_form=Loginform) ,name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html', form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html' ,form_class= MySetPasswordForm),name= "password_reset_confirm") ,
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
admin.site.site_header="MangalAgro Shop"
admin.site.site_title="MangalAgro Shop"
admin.site.site_indder_title="MangalAgro Shop"


# <small class="fw-light text-decoration-line-through">{{prod.price}}</small>