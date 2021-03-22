from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ='park-home'),      
    path('login/', views.login, name ='park-login'),      
]