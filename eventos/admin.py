from django.contrib import admin

# Register your models here.
from .models import Evento, Participante
admin.site.register(Evento)
admin.site.register(Participante)