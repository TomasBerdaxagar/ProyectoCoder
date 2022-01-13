from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Jugador)

admin.site.register(Estadio)

admin.site.register(Liga)

admin.site.register(Avatar)
