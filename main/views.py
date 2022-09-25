from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def get_user_details(request):
    if request.user != None:
        return HttpResponse('Email :'+request.user.email+'user_type:'+request.user.user_type)
    else:
        return HttpResponse('please login first')

def logout_user(reqeust):
    logout(reqeust)
    return HttpResponseRedirect('/')

def loginpage(request):
    return render(request,'login.html',{})

def doLogin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method Not Allowed</h2>')
    else:
        email = request.POST['email']    
        password = request.POST['password']    
        user = EmailBackEnd.authenticate(request,username=email,password=password)
        if user !=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse('<h2>Admin login</h2>')
            elif user_type == '2':
                return HttpResponse('<h2>Staff login</h2>')  
            elif user_type == '3':
                return HttpResponse('<h2>Student login</h2>')  
            else:
                messages.error(request,'passwor or email is invalid')
                return HttpResponse('<h2>login page<h2>')    
        return HttpResponse('<h2>login page<h2>')                                                      


