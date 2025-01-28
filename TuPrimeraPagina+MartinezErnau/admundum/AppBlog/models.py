from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def _str_(self):
        return self.nombre

class Autor(models.Model):
    class Estado(models.TextChoices):
        ACTIVE = '1', 'Activo'
        INACTIVE = '0' , 'Inactivo'

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nick = models.CharField(max_length=100)
    status = models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVE)

    def _str_(self):
        return self.nick

class Posteo(models.Model):
    titulo = models.CharField(max_length=250)
    resumen = models.CharField(max_length=250)
    texto = models.TextField() 
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)

