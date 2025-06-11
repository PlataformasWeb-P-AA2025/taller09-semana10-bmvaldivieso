from django.contrib import admin
from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos  

# Clase personalizada para administrar el modelo EquipoFutbol
class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'username_twitter')  # Atributos que se mostrarán en la lista de registros
    search_fields = ('nombre', 'siglas')  # Campos por los que se podrá buscar

# Clase personalizada para administrar el modelo Jugador
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo_futbol')  # Atributos visibles
    search_fields = ('nombre', 'posicion_campo')  # Campos de búsqueda
    list_filter = ('equipo_futbol',)  # Filtro lateral por equipo

# Clase personalizada para administrar el modelo Campeonato
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_campeonato', 'nombre_auspiciante')  # Atributos visibles en la lista
    search_fields = ('nombre_campeonato',)  # Búsqueda por nombre del campeonato

# Clase personalizada para administrar el modelo CampeonatoEquipos
class CampeonatoEquiposAdmin(admin.ModelAdmin):
    list_display = ('equipo_futbol', 'campeonato', 'año')  # Atributos visibles
    search_fields = ('equipo_futbol__nombre', 'campeonato__nombre_campeonato')  # Búsqueda por nombre relacionado
    list_filter = ('año', 'campeonato')  # Filtros por año y campeonato

# Registro de cada modelo con su clase admin correspondiente para que aparezcan en el panel de administración
admin.site.register(EquipoFutbol, EquipoFutbolAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
