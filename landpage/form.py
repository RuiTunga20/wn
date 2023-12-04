from django import forms
from .models import Inscricao,Empresa,encontrosb2b,EmpresaPatrocinio,Inscricao_empresa

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        exclude = ['estado','image','user_updadte']
    
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'urt': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'Convidados': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'Evento': forms.Select(attrs={'class': 'form-control'}),                        

          
           
        }

    

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        exclude = ['estado','image','user_updadte']
    
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'urt': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'Convidados': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'Evento': forms.Select(attrs={'class': 'form-control'}),                        

          
           
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        exclude = ['estado', 'image', 'user_updadte']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'Pacotes': forms.Select(attrs={'class': 'form-control'}),
        }
 



class encontrosb2bForm(forms.ModelForm):
    class Meta:
        model = encontrosb2b
        exclude = ['estado', 'image', 'user_updadte']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'Pacotes': forms.Select(attrs={'class': 'form-control'}),
        }

class EmpresaFormPatrocinio(forms.ModelForm):
    class Meta:
        model = EmpresaPatrocinio
        exclude = ['estado', 'image', 'user_updadte']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'Pacotes': forms.Select(attrs={'class': 'form-control'}),
        }


class Inscricao_empresaForm(forms.ModelForm):
    class Meta:
        model = Inscricao_empresa
        exclude = ['image','user_updadte','empresa']
    
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),

          
           
        }
