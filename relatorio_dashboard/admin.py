from django.contrib import admin
from .models import Despesas, Vendas, Vendedor, Produto, Despesas
# Register your models here.

admin.site.register(Vendas)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Despesas)