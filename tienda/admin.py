from django.contrib import admin
from .models import CategoriaProd,Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=("nombre","id")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=("id","nombre","categorias","imagen","precio","created","updated")
    search_fields=("nombre","precio")
    list_filter=("categorias","created")
    date_hierarchy=("created")

admin.site.register(CategoriaProd,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)