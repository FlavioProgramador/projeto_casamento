from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    TIPOS = (
        ('cliente', 'Cliente'),
        ('fornecedor', 'Fornecedor'),
        ('cerimonialista', 'Cerimonialista'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS)

class Cliente(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=18, unique=True, default='00000000000000')

    def __str__(self):
        return f"{self.usuario.username}"

from django.db import models

class Fornecedor(models.Model):
    CATEGORIAS = [
        ('buffet', 'Buffet'),
        ('decoracao', 'Decoração'),
        ('som_iluminacao', 'Som e Iluminação'),
        ('fotografia', 'Fotografia'),
        ('video', 'Filmagem / Vídeo'),
        ('bolo_doces', 'Bolo e Doces'),
        ('musica', 'Música / Banda / DJ'),
        ('transporte', 'Transporte / Limousine'),
        ('vestuario', 'Vestuário / Noivos e Convidados'),
        ('beleza', 'Beleza / Maquiagem e Cabelo'),
        ('convites', 'Convites e Papelaria'),
        ('aluguel_moveis', 'Aluguel de Móveis e Estruturas'),
        ('entretenimento', 'Entretenimento / Shows'),
        ('seguranca', 'Segurança'),
        ('outros', 'Outros'),
    ]

    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_empresa = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    cpf_cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nome_empresa} - {self.categoria}"
    

class Cerimonialista(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(max_length=18, unique=True, default='00000000000000')
    empresa = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username}"
