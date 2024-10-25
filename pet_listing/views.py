from django.shortcuts import redirect, render, get_object_or_404
from .models import Pet

def adopter_pet_list(request):
    query = request.GET.get('q', '')
    pets = Pet.objects.all() 
    if query:
        pets = pets.filter(name__icontains=query)
    return render(request, 'adopter_pet_list.html', {'pets': pets , 'query': query,})

def view_pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'view_pet.html', {'pet': pet})
