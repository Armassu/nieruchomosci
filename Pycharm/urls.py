from django.contrib import admin
from django.urls import path
from .views import moj_widok, inny_widok  # Dodaj import nowego widoku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moj-widok/', moj_widok, name='moj_widok'),  # Dodaj nowy URL dla moj_widok
    path('inny-widok/', inny_widok, name='inny_widok'),  # Dodaj nowy URL dla inny_widok
]
