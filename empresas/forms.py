from django import forms

from empresas.models import Company, Jobs, Specializations, Technologies


class CadastroEmpresa(forms.ModelForm):
    
    name = forms.CharField(label = '', widget=forms.TextInput(attrs = {'placeholder': 'Nome da Empresa'}))

    class Meta:
        model = Company
        fields = '__all__'

    technologies = forms.ModelMultipleChoiceField(
        queryset= Technologies.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    specializations = forms.ModelMultipleChoiceField(
        queryset= Specializations.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    def clean_logo(self):
        data =  self.cleaned_data.get('logo')
        filesize= data.size
    
        if filesize > 100_000_000:
            raise forms.ValidationError("You cannot upload file more than 10Mb")
        else:
            return data

class CadastroVaga(forms.ModelForm):
    
    class Meta:
        model = Jobs
        fields = '__all__'

    title = forms.CharField(label = '', widget=forms.TextInput(attrs = {'placeholder': 'Título da Vaga'}))
