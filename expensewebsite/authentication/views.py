from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json 
from validate_email import validate_email  
# Create your views here.

class EmailValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        
        if User.objects.filter(email=email).exists() :
            return JsonResponse({'email_error':'This email is already registered.Please choose another one'},status=409)
        
        return JsonResponse({'email_valid':True})

class UsernameValidationView(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric'},status=400)
        
        if User.objects.filter(username=username).exists() :
            return JsonResponse({'username_error':'Username already taken.Please choose another one'},status=409)
        
        return JsonResponse({'username_valid':True})
        

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
        

 