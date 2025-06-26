from django.db import models
from apps.usuario.models import Cerimonialista, Cliente, Fornecedor

# Create your models here.

class StatusChoices(models.TextChoices):
    PLANEJADO = 'planejado', 'Planejado'
    EM_ANDAMENTO = 'em_andamento', 'Em Andamento'
    CONCLUIDO = 'concluido', 'Concluído'
    CANCELADO = 'cancelado', 'Cancelado'

class Casamento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    local = models.CharField(max_length=200)

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PLANEJADO
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cerimonialista = models.ForeignKey(Cerimonialista, on_delete=models.SET_NULL, null=True, blank=True)
    fornecedores = models.ManyToManyField(Fornecedor, blank=True)


    def __str__(self):
        return self.titulo
