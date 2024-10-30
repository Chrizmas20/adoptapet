from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name="login"),
    path('register/adopter', views.Register, name="adopter_register"),
    path('register/admin', views.Register, name="admin_register"),
]