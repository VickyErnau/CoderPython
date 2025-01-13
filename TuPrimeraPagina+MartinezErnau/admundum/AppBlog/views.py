
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Posteo, Categoria,Autor
from .forms import CategoriaForm, AutorForm, PosteoForm

# Create your views here.

def inicio(request):
    return render(request, "index.html")

#---------------------------------
# CATEGORIAS
#---------------------------------

def categoria_form(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        
        if form.is_valid():
            categoria = Categoria(nombre=form.cleaned_data['nombre'])
            categoria.save()
            return redirect('inicio')
        else:
            print("Operación Incorrecta!")

    form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form':form})

def categoria_index(request):
    categorias = Categoria.objects.all().order_by("nombre")
    context = {
        "categorias": categorias,
    }
    return render(request, "categoria.html", context)

#---------------------------------
#AUTORES
#---------------------------------

def autor_form(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        
        if form.is_valid():
            autor = Autor(nombre=form.cleaned_data['nombre'],apellido=form.cleaned_data['apellido']
                        ,nick=form.cleaned_data['nick'],status=form.cleaned_data['status'])
            autor.save()
            return redirect('inicio')
        else:
            print("Operación Incorrecta!")

    form = AutorForm()
    return render(request, 'autor_form.html', {'form':form})

def autor_index(request):
    autores = Autor.objects.all().order_by("nombre")
    context = {
        "autores": autores,
    }
    return render(request, "autor.html", context)

def autor_buscar(request):
    query = request.GET.get("q")
    autores = Autor.objects.all()
    
    if query:
        autores = Autor.objects.filter(
            Q(nombre__icontains = query) |
            Q(apellido__icontains = query) |
            Q(nick__icontains = query) 
        ).distinct()
    
    return render(request,'autor.html',{'autores': autores})
            
#---------------------------------
#POSTEOS
#---------------------------------

def posteo_form(request):
    if request.method == "POST":
        form = PosteoForm(request.POST)
        print(f'{form}')
        if form.is_valid():

            autor_selected = Autor.objects.get(id=form.cleaned_data['autor'])
            categoria_selected = Categoria.objects.get(id=form.cleaned_data['categoria'])

            posteo = Posteo(titulo=form.cleaned_data['titulo'],resumen=form.cleaned_data['resumen']
                        ,texto=form.cleaned_data['texto'], autor=autor_selected 
                        ,categoria=categoria_selected) 
            posteo.save()
            return redirect('inicio')
        else:
            print("Operación Incorrecta!")

    form = PosteoForm()
    return render(request, 'posteo_form.html', {'form':form})

def posteo_index(request):
    posts = Posteo.objects.all().order_by("-create_date")
    context = {
        "posts": posts,
    }
    return render(request, "post.html", context)

