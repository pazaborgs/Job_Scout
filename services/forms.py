from django import forms
from services.models import Service

class NewService(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ["owner"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'price_range': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'service_type': forms.Select(attrs={'class': 'form-control mb-3'}),
        }