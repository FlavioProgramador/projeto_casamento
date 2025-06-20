from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome