from django.urls import path
from .import views

urlpatterns =[
    path('buyerhomepage/', views.buyerhomepage, name="buyerhomepage"),
    path ('buyersignuppage/',views.buyersignup,name='buyerSignupPage'),
    path('buyerloginpage/',views.buyerlogin,name='buyerLoginPage'),
    path ('buyerloginsuccessfull/',views.buyerloginsuccessfull,name='buyerLoginSuccessfullPage'),
    path('orderHistory/', views.orderHistory,name="orderHistory"),
    path('makeOrder/',views.makeOrder,name="makeOrder")
]