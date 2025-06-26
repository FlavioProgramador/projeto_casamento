from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Cliente, Fornecedor, Cerimonialista


# Formulário para usuário base (com senha)
class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


# Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefone', 'cpf']


# Fornecedor
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_empresa', 'cpf_cnpj', 'categoria']


# Cerimonialista
class CerimonialistaForm(forms.ModelForm):
    class Meta:
        model = Cerimonialista
        fields = ['cpf_cnpj', 'empresa']
