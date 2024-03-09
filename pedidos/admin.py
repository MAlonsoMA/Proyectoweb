from django.contrib import admin
from . models import Pedido,LineaPedido

# Register your models here.
admin.site.register(LineaPedido)
admin.site.register(Pedido)
