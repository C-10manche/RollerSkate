from django import forms
from .models import Inventory, RollerSkate

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "address"]
        
class RollerSkateForm(forms.ModelForm):
    class Meta:
        model = RollerSkate
        fields = ["name", "size_min", "size_max", "barcode", "inventory"]
