from django.shortcuts import render

# Create your views here.
def adopter_profile(request):
    return render(request, 'view_pet.html')