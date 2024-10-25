from django.urls import path
from . import views 

urlpatterns = [
    path('', views.adopter_profile, name='adopter_profile'),
]