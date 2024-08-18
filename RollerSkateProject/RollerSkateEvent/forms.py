from django import forms
from .models import Event, Client, Order

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_time", "end_time", "inventories"]
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'format': '%Y-%m-%dT%H:%M'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'format': '%Y-%m-%dT%H:%M'}),
            'inventories': forms.CheckboxSelectMultiple(),
        }        
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email", "age"]