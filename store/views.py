from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Plant
from django.urls import reverse_lazy
from .mixin import AuthenticatedUserMixin, AuthenticatedStaffMixin


class PlantsListView(AuthenticatedUserMixin, ListView):
    model = Plant
    template_name = 'store/plants_list.html'
    context_object_name = 'plants'


class PlantDetailView(AuthenticatedUserMixin, DetailView):
    model = Plant
    template_name = 'store/plant_detail.html'
    context_object_name = 'plant'


class PlantCreateView(AuthenticatedStaffMixin, CreateView):
    model = Plant
    fields = ['title', 'description', 'price']
    template_name = 'store/plant_form.html'
    success_url = reverse_lazy('plant-list')


class PlantUpdateView(AuthenticatedStaffMixin, UpdateView):
    model = Plant
    fields = ['title', 'description', 'price']
    template_name = 'store/plant_edit.html'

    def get_success_url(self):
        return reverse_lazy('plant-detail', kwargs={'pk': self.object.pk})


class PlantDeleteView(AuthenticatedStaffMixin, DeleteView):
    model = Plant
    template_name = 'store/plant_delete.html'
    success_url = reverse_lazy('plant-list')