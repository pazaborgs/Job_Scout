from django import forms
from empresas.models import Company, Jobs

class CadastroEmpresa(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ["owner"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'headquarters': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'company_size': forms.Select(attrs={'class': 'form-control mb-3'}),
            'marketing_niche': forms.Select(attrs={'class': 'form-control mb-3'}),
            'logo': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }

    def clean_logo(self):
        data = self.cleaned_data.get('logo')
        default_logo_path = 'static/assets/helmet_bro.jpg'

        if data is None:
            return default_logo_path
        
        filesize = data.size
        if filesize > 10 * 1024 * 1024:  # 10MB in bytes
            raise forms.ValidationError("Você não pode enviar um arquivo maior que 10MB")
        return data

class CadastroVaga(forms.ModelForm):
    
    class Meta:
        model = Jobs
        fields = '__all__'

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
                'experience': forms.Select(attrs={'class': 'form-control mb-3'}),
                'url': forms.URLInput(attrs={'class': 'form-control mb-3'}),
                'final_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
                'position_type': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
                'status': forms.Select(attrs={'class': 'form-control mb-3l'}),
            }