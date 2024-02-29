from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from newdevelop.views import *
from django.urls import path, include

urlpatterns = [
    
    
    

    path('viewlogin',viewlogin),
    path('admin/', admin.site.urls),
    path('',index,name=""),
    path("login",login,name="login"),
    path("logout",logout,name='logout'),
    path("main",main,name="main"),
    path("internal",internal,name="internal"),
    path("employee",employee,name="employee"),
    path("loginadmin",loginadmin,name="loginadmin"),
    path("response/<str:pk>",response,name='response'),
    path("videologin",videologin,name='videologin'),
    path('video',video,name='video'),
    path("profiles",profiles,name='profile'),
    path("profile",profile),
    path("api/<str:pk>/",EmployeeDetails.as_view()),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
   
