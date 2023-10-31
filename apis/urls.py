from django.urls import path
from .views import PlantAPIView

urlpatterns = [
    path('', PlantAPIView.as_view(), name='plant-list-api'),
]
