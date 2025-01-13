from django.urls import path
from .views import inicio, posteo_form, autor_form, categoria_form, posteo_index, categoria_index
from .views import autor_buscar, autor_index

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("posteo-nuevo/", posteo_form, name="posteo_form"),
    path("posts/", posteo_index, name="posteo_index"),
    path("categoria-nueva/", categoria_form, name="categoria_form"),
    path("categorias/", categoria_index, name="categoria_index"),
    path("autor-nuevo/", autor_form, name="autor_form"),
    path("autores/", autor_buscar, name="autor_index"),
]
