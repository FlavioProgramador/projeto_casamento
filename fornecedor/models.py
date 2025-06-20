from django.db import models
from usuario.models import Usuario

# Create your models here.

class Fornecedor(Usuario):
    senha = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome