from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
from .models import Employee
from .serializers import *
from django.http import HttpResponse
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView






# Create your views here.

    
def index(request):
 if request.method =='POST': 
      
     firstname=request.POST['first']
     lastname=request.POST['lastname']
     email=request.POST['email']
     username=request.POST['username']
     contact=request.POST['contact']
     country=request.POST['country']
     password1=request.POST['password1']
     password2=request.POST['password2']
     if password1 == password2:
         if Feature.objects.filter(email=email).exists():
            
            messages.info(request,'Email is already Used')
            return redirect('/')
         elif Feature.objects.filter(username=username).exists():
            messages.info(request,'User Name Already used')
            return redirect('/')
         else:
            user=Feature(firstname=firstname,lastname=lastname,email=email,username=username,contact=contact,country=country,password1=password1)
            
            user.save();
            return render(request,'login.html')
      
     else:
         messages.info(request,'Password not same')
         
         return redirect('/')
 else:    
    
   return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['user_name']
        password=request.POST['password']
        user=Feature.objects.filter(username=username,password1=password)
        if  user is not None:
            return redirect('main')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        
      return redirect('login')
  
  
def logout(request):
    auth.logout(request)
    return redirect('/')



def internal(request):
   
     return render(request,'internal.html')


def employee(request):
  if request.method =='POST':
     firstname=request.POST['firstname']
     lastname=request.POST['lastname']
     employeeid=request.POST['employeeid']
     city=request.POST['city']
     state=request.POST['state']
     zip=request.POST['zip']
     email=request.POST['email']
     current_salary=request.POST['current_salary']
     expected_salary=request.POST['expected_salary']
     current_domain=request.POST['current_domain']
     change_domain=request.POST['change_domain']
     skills=request.POST['skills']
     if firstname=="":
         messages.info(request,'first name not take empty')
         return redirect('employee')
     elif lastname=="":
         messages.info(request,'lastname name not take empty')
         return redirect('employee')
     elif Employee.objects.filter( employeeid=employeeid):
            messages.info(request,'This Employee already Exists')
            return redirect('employee')

         
     elif employeeid=="":
         messages.info(request,'employeeid name not take empty')
         return redirect('employee')
     elif city=="":
         messages.info(request,' currentcity not take empty')
         return redirect('employee')
     elif state=="":
         messages.info(request,'state not take empty')
         return redirect('employee')
     elif zip=="":
         messages.info(request,'zip not take empty')
         return redirect('employee')
     elif email=="":
         messages.info(request,'email not take empty')
         return redirect('employee')
     elif current_salary=="":
         messages.info(request, 'current_salary take empty')
         return redirect('employee')
     elif expected_salary=="":
         messages.info(request,'expected_salary not take empty')
         return redirect('employee')
     elif current_domain=="":
         messages.info(request,'current_domain not take empty')
         return redirect('employee')
     elif skills=="":
         messages.info(request,'skills not take empty')
         return redirect('employee')
     
     else:
      user=Employee(firstname=firstname,lastname=lastname,employeeid=employeeid,city=city,state=state,zip=zip,email=email,current_salary=current_salary,expected_salary=expected_salary,current_domain=current_domain,change_domain=change_domain,skills=skills)
            
      user.save();
      return render(request,'Thanks.html')
  else:    
    
      return render(request,'internal.html')
 
def main(request):
    return render(request,'main.html')

def loginadmin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            posts=Employee.objects.all()
            return render(request,'admins.html',{'posts':posts})

            
        else:
            messages.info(request,'credentials Invalid')
            return redirect('loginadmin')
            
    else:
        return render(request,'adminform.html')
     
    
def response(request,pk):
    posts=Employee.objects.get(id=pk)
    
    return render(request,'mails.html',{'posts':posts})   

def video(request):
     return render(request,'video.html')
    

def videologin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('video')
        else:
            messages.info(request,'credentials Invalid')
            return redirect('videologin')
            
    else:
        return render(request,'videologin.html')
    
def profile(request):
    if request.method=='POST':
        username=request.POST['first']
        ids=request.POST['id']
        #posts=Employee.objects.all()
        
        posts=Employee.objects.filter(employeeid=ids,firstname=username)
        if posts.exists():
            return render(request,'test.html',{'posts':posts})
        else:
            messages.info(request,'credentials Invalid')
            return redirect('profile')
                
          
        
            
def profiles(request):
         return render(request,'profile.html')
     
     
     
class EmployeeDetails(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
     queryset=Employee.objects.all()
     serializer_class=Employeeserializer

def viewlogin(request):
    return render(request,'login.html')
            
            

            


    

            
          
          
          
          
          
        
    
    
       
    
     
        







