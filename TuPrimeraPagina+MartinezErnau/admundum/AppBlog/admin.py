from django.contrib import admin

# Register your models here.

from .models import Categoria, Autor, Posteo

@admin.register(Categoria)
class CategriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','nick','status')
    search_fields = ('nombre','apellido','nick')
    list_filter = ('status',)
    ordering = ('-status','nick',)


@admin.register(Posteo)
class PosteoAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria','autor')
    search_fields = ('titulo','categoria','autor')
    list_filter = ('categoria',)
    ordering = ('categoria',)