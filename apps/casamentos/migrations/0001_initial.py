# Generated by Django 5.1.7 on 2025-06-20 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cerimonialista', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('local', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('planejado', 'Planejado'), ('em_andamento', 'Em Andamento'), ('concluido', 'Concluído'), ('cancelado', 'Cancelado')], default='planejado', max_length=20)),
                ('cerimonialista_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cerimonialista.cerimonialista')),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
        ),
    ]
