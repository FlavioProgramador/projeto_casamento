from django.db import models
from apps.cerimonialista.models import Cerimonialista
from apps.cliente.models import Cliente


# Create your models here.

class Casamento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    local = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[
        ('planejado', 'Planejado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado')
    ], default='planejado')
    cerimonialista_id = models.ForeignKey(Cerimonialista, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
