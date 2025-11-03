from django import forms
from datetime import date


class EventoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    fecha = forms.DateField(required=True)
    ubicacion = forms.DateField(required=False)

    def clean_fecha(self):
        hoy = date.today()
        fecha = self.cleaned_data['fecha']
        if fecha <= hoy:
            raise forms.ValidationError("El evento debe estar organizado en una fecha futura.")
        return fecha
    
    def __str__(self):
        return super().__str__()
    
class ParticipanteForm(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.EmailField(required=True)