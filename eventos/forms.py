from django import forms
from datetime import date

from eventos.models import Evento, Participante

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']
        labels = {
            'nombre': 'Nombre del Evento',
            'fecha': 'Fecha del Evento',
            'ubicacion': 'Ubicación del Evento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'maxlength': 100}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'ubicacion': forms.TextInput(),
        }
    def clean_fecha(self):
        hoy = date.today()
        fecha = self.cleaned_data['fecha']
        if fecha <= hoy:
            raise forms.ValidationError("El evento debe estar organizado en una fecha futura.")
        return fecha

class ParticipanteForm(forms.ModelForm): 
    class Meta:
        model = Participante
        fields = ['nombre', 'email', 'evento']
        labels = {
            'nombre': 'Nombre del Participante',
            'email': 'Email del Participante',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'maxlength': 100}),
            'email': forms.EmailInput(),
        }
