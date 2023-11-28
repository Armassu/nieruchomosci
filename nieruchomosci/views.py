from django.shortcuts import render
from .models import Nieruchomosc

def moj_widok(request):
    # Pobranie wszystkich obiektów z modelu Nieruchomosc
    zestaw_danych = Nieruchomosc.objects.all()

    # Przekazanie zestawu danych do szablonu jako kontekstu
    return render(request, 'moj_szablon.html', {'zestaw_danych': zestaw_danych})

def inny_widok(request):
    # Dodaj dowolną logikę dla innego widoku
    return render(request, 'inny_szablon.html')
