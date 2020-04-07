# H2Blog / user / urls.py
# Bu url sayfasını yapmaktaki maksat daha fazla url adresinin ana dizindeki url sayfasına yığılamasını engellemek

from django.contrib import admin
from django.urls import path

# Şu anki klasördeki views'i al
from . import views 

# uygulamamızın adı: 
app_name = "user"

urlpatterns = [
    path('register', views.register,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    
      
]