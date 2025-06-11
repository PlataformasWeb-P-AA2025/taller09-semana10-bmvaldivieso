from django.db import models

# Modelo que representa un equipo de fútbol
class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del equipo 
    siglas = models.CharField(max_length=10)  # Siglas del equipo 
    username_twitter = models.CharField(max_length=50)  # Usuario de Twitter del equipo

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"  

# Modelo que representa un jugador de fútbol
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre completo del jugador
    posicion_campo = models.CharField(max_length=50)  # Posición del jugador en el campo
    numero_camiseta = models.IntegerField()  # Número de camiseta del jugador
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)  # Sueldo con dos decimales
    # Relación con el equipo al que pertenece
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.nombre} - {self.posicion_campo} - #{self.numero_camiseta}"  

# Modelo que representa un campeonato de fútbol
class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)  # Nombre del campeonato
    nombre_auspiciante = models.CharField(max_length=100)  # Nombre del patrocinador

    def __str__(self):
        return self.nombre_campeonato  

# Modelo que relaciona equipos con campeonatos en un determinado año
class CampeonatoEquipos(models.Model):
    año = models.IntegerField()  # Año en el que el equipo participa en el campeonato
    # Relación con el equipo participante
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    # Relación con el campeonato al que pertenece  
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.equipo_futbol.nombre} en {self.campeonato.nombre_campeonato} ({self.año})"
