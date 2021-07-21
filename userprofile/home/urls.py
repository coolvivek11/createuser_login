from django.urls import path, include
from home import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('userlogout', views.userlogout, name='userlogout'),
    path('signup', views.signup, name='signup'),
]
