from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponse
from .models import farmer_detail
# Create your views here.
def farmerhomepage(request):
    return render(request, 'farmerhomepage.html',{})

def farmersSignup(request):
    if request.method =='POST':
        farmerUsername = request.POST.get('farmerUsername')
        farmerNumber= request.POST.get ('farmerNumber')
        farmerPassword= request.POST.get('fpassword')
        farmerEmail=request.POST.get('email')
        farmerAddress= request.POST.get('farmerAddress')
        new_farmer = User.objects.create_user(username=farmerUsername,email=farmerEmail,password=farmerPassword)
        new_farmer.save()
        dbfarmers=farmer_detail(dbfarmerUsername=farmerUsername,dbfarmerPassword=farmerPassword,dbfarmerEmail=farmerEmail,dbfarmerPhonenum=farmerNumber,dbfarmerAddress=farmerAddress)
        dbfarmers.save()
        return redirect ('farmerlogin.html')
    return render(request, 'farmerSignup.html')

def farmerLogin(request):
   if request.method =='POST':
       Username =request.POST.get('lfusername')
       Password = request.POST.get('lfpassword')
       
       farmer= authenticate (request, username=Username, password=Password)
       if farmer is not None:
           login(request, farmer)
           return redirect('loginsuccess.html')
       else:
            return HttpResponse ('Error, user does not exist')
           
   return render(request,'farmerlogin.html',{})
def farmerloginsuccess(request):
    return render(request, 'loginsuccess.html',{})

def farmerLogout(request):
    logout (request)
    return redirect ('farmerlogin.html')
