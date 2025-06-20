from django.contrib import admin
from apps.financeiro.models import Financeiro, Parcela
# Register your models here.
admin.site.register(Financeiro)
admin.site.register(Parcela)