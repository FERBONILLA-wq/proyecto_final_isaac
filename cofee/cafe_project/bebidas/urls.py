from django.urls import path
from .views import iniciar_sesion, home

urlpatterns = [
    path('', iniciar_sesion, name='login'),
    path('home/', home, name='home'),
    # Otras URLs
]
