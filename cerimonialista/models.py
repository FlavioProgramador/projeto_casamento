from django.db import models
from usuario.models import Usuario

# Create your models here.

class Cerimonialista(Usuario):
    senha = models.CharField(max_length=100, unique=True)
    cpf_cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome
