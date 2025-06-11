from django.db import models

# Create your models here.
from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.posicion_campo} - #{self.numero_camiseta}"

class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    nombre_auspiciante = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_campeonato

class CampeonatoEquipos(models.Model):
    año = models.IntegerField()
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipo_futbol.nombre} en {self.campeonato.nombre_campeonato} ({self.año})"

