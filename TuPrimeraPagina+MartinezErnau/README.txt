* Se mencionan debajo las URLs que pueden ser utilizadas. 

* Accediendo al inicio hay una barra de navegación con todos los links necesarios
  por lo que no debería ser necesario tener que ingresar a las distintas urls de manera directa.

* El buscador está implementado únicamente para los autores.

* En el caso de dar de alta Categorías y/o Autores y querer utilizarlas para crear nuevos posteos, es necesario bajar y volver a levantar el servidor ya que no está implementado el refresh automático.

URLs

path("inicio/", inicio, name="inicio"),
path("posteo-nuevo/", posteo_form, name="posteo_form"),
path("posts/", posteo_index, name="posteo_index"),
path("categoria-nueva/", categoria_form, name="categoria_form"),
path("categorias/", categoria_index, name="categoria_index"),
path("autor-nuevo/", autor_form, name="autor_form"),
path("autores/", autor_buscar, name="autor_index"),



