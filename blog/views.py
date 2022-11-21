from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter()
    return render(request, 'animal_list.html', {'animals': animals})

def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieu = animal.lieu
    form=MoveForm()
    return render(request,
                  'animal_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form})

# Create your views here.
