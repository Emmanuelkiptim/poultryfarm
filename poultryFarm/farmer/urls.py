from django.urls import path
from.views import farmerhomepage,farmersSignup,farmerLogin,farmerloginsuccess,farmerLogout

urlpatterns= [
    path ('farmerhomepage/',farmerhomepage,name='farmerhomepage.html'),
    path ('farmersignuppage/',farmersSignup,name='farmerSignup.html'),
    path('farmerloginpage/',farmerLogin,name='farmerlogin.html'),
    path ('farmerloginsuccessfull/',farmerloginsuccess,name='loginsuccess.html'),
    path('farmerlogout/',farmerLogout,name='farmerLogout.html'),
]
