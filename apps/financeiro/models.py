from django.db import models
from apps.casamentos.models import Casamento

# Create your models here.

class Financeiro(models.Model):
    TIPO_CHOICES = [
        ('Receber', 'Receber'),
        ('Pagar', 'Pagar'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor_total = models.FloatField()
    data = models.DateField()
    descricao = models.TextField()
    casamento = models.ForeignKey(Casamento, on_delete=models.CASCADE)

class Parcela(models.Model):
    valor = models.FloatField()
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    financeiro = models.ForeignKey(Financeiro, on_delete=models.CASCADE)
