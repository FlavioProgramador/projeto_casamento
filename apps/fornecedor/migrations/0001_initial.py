# Generated by Django 5.1.7 on 2025-06-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=100, unique=True)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('categoria', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
