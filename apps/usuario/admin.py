from django.contrib import admin
from .models import CustomUser, Cerimonialista, Fornecedor, Cliente

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Cerimonialista)
admin.site.register(Fornecedor)
admin.site.register(Cliente)