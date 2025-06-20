from django.db import models
from apps.casamentos.models import Casamento
from apps.cerimonialista.models import Cerimonialista
from apps.cliente.models import Cliente
from apps.fornecedor.models import Fornecedor

# Create your models here.

class Contrato(models.Model):
    STATUS_CHOICES = [
        ('Assinado', 'Assinado'),
        ('Pendente', 'Pendente'),
    ]

    data_assinatura = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    casamento = models.ForeignKey(Casamento, on_delete=models.CASCADE)
    cerimonialista = models.ForeignKey(Cerimonialista, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
