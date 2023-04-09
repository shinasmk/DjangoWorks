from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,UpdateView,DetailView
from vehicle.models import Vehicles
from vehicle.forms import VehicleForm
from django.urls import reverse_lazy
# Create your views here.



class VehicleCreateView(CreateView):
    model=Vehicles
    form_class=VehicleForm
    template_name="vehicle-add.html"
    success_url=reverse_lazy("vehicle-add")


class VehicleListView(ListView):
    model=Vehicles
    context_object_name="vehicles"
    template_name="vehicle-list.html"

class VehicleDetailView(DetailView):
    model=Vehicles
    context_object_name="vehicles"
    template_name="vehicle-detail.html"

class VehicleEditView(UpdateView):
    model=Vehicles
    form_class=VehicleForm
    template_name="vehicle-edit.html"
    success_url=reverse_lazy("vehicle-list")

class VehicleDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Vehicles.objects.get(id=id).delete()
        return redirect("vehicle-list")
