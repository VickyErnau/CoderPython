from django import forms
from .models import Categoria,Autor

class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nick = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=Autor.Estado.choices)

    def __str__(self):
        return self.nombre

class PosteoForm(forms.Form):
    class categorias():
        opciones = {}
        for x in Categoria.objects.all():
            opciones[x.id] = x.nombre

    class autores():
        opciones = {}
        for x in Autor.objects.all():
            opciones[x.id] = x.nick

    titulo = forms.CharField(max_length=250)
    resumen = forms.CharField(max_length=250, widget=forms.Textarea)
    texto = forms.CharField(widget=forms.Textarea)
    autor = forms.ChoiceField(choices=autores.opciones)
    categoria = forms.ChoiceField(choices=categorias.opciones)
    
    
