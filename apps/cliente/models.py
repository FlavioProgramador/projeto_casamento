from django.db import models
from apps.usuario.models import Usuario

# Create your models here.

class Cliente(Usuario):
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome