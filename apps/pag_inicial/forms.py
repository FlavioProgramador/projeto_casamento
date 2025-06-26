from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Cliente, Fornecedor, Cerimonialista


# FORM DE USUÁRIO PERSONALIZADO
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'tipo', 'password1', 'password2']


# FORMULÁRIO DE CLIENTE
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefone', 'cpf']


# FORMULÁRIO DE FORNECEDOR
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_empresa', 'cpf_cnpj', 'categoria', 'portfolio', 'descricao']


# FORMULÁRIO DE CERIMONIALISTA
class CerimonialistaForm(forms.ModelForm):
    class Meta:
        model = Cerimonialista
        fields = ['cpf_cnpj', 'empresa']


# FORM DE LOGIN PERSONALIZADO (opcional)
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='E-mail ou Usuário')
    password = forms.CharField(widget=forms.PasswordInput)
