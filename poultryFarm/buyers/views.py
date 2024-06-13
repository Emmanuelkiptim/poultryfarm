from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import buyerdb
# Create your views here.
def buyerhomepage(request):
    return render(request, 'buyerhomepage.html',{})
    #return HttpResponse("hello world!")

def buyersignup(request):
    if request.method =='POST':
        buyerUsername = request.POST.get('buyerUsername')
        buyerNumber= request.POST.get ('buyerNumber')
        buyerPassword= request.POST.get('buyerPassword')
        buyerAddress= request.POST.get('buyerAddress')
        new_buyer=User.objects.create_user(username=buyerUsername,password=buyerPassword)
        new_buyer.save()
        dbuyer=buyerdb(buyerUsername=buyerUsername,buyerPassword=buyerPassword,buyerPhonenum=buyerNumber,buyerAddress=buyerAddress)
        dbuyer.save()
        #new_buyerInDb.save()
        return redirect ('buyerLoginPage')
        
    return render(request, 'buyersignup.html')

def buyerlogin(request):   
    if request.method =='POST':
       Username =request.POST.get('lbusername')
       Password = request.POST.get('lbpassword')
       
       buyer= authenticate (request, username=Username, password=Password)
       if buyer is not None:
           login(request, buyer)
           return redirect('buyerLoginSuccessfullPage')
       else:
            return redirect ('buyerLoginPage')
    return render (request,'buyerlogin.html')
def buyerloginsuccessfull(request):
    return render( request,'buyersuccesslogin.html')
def orderHistory(request):
    return render(request, 'orderHistory.html' )
def makeOrder(request):
    return render (request, 'makeOrder.html' )