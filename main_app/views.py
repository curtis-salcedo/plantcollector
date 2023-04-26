from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Fertilizer
from .forms import WateringForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants
    })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    # fertilizer = plant.fertilizers.all()
    id_list = plant.fertilizers.all().values_list('id')
    fertilizers_plant_doesnt_have = Fertilizer.objects.exclude(id__in=id_list)
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {
        'plant': plant,
        'watering_form': watering_form,
        'fertilizers': fertilizers_plant_doesnt_have,
        # 'fertilizer': fertilizer,
    })

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'type', 'description']

class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'

class FertilizerList(ListView):
    model = Fertilizer

class FertilizerDetail(DetailView):
    model = Fertilizer
    fields = '__all__'

class FertilizerCreate(CreateView):
    model = Fertilizer
    fields = '__all__'

class FertilizerUpdate(UpdateView):
    model = Fertilizer
    fields = ['name', 'description']

class FertilizerDelete(DeleteView):
    model = Fertilizer
    success_url = '/fertilizers'

def assoc_fertilizer(request,  plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
    return redirect('detail', plant_id=plant_id)

def unassoc_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.remove(fertilizer_id)
    return redirect('detail', plant_id=plant_id)