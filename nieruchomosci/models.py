from django.db import models

class Nieruchomosc(models.Model):
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    metraz = models.DecimalField(max_digits=6, decimal_places=2)
    liczba_pokoi = models.IntegerField()
    zdjecie = models.ImageField(upload_to='zdjecia_nieruchomosci/')
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul
