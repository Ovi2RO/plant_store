from django.urls import path
from .views import (
    PlantsListView, 
    PlantDetailView,
    PlantCreateView,
    PlantUpdateView,
    PlantDeleteView
    )

urlpatterns = [
    path('', PlantsListView.as_view(), name='plant-list'),
    path('<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('create/', PlantCreateView.as_view(), name='plant-create'),
    path('<int:pk>/edit/', PlantUpdateView.as_view(), name='plant-edit'),
    path('<int:pk>/delete/', PlantDeleteView.as_view(), name='plant-delete'),
]
