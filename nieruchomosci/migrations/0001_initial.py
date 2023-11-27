# Generated by Django 4.2.6 on 2023-10-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nieruchomosc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('opis', models.TextField()),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metraz', models.DecimalField(decimal_places=2, max_digits=6)),
                ('liczba_pokoi', models.IntegerField()),
                ('zdjecie', models.ImageField(upload_to='zdjecia_nieruchomosci/')),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
