from django.db import models

# Create your models here.

class Registrado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    localidad=models.CharField(max_length=20)
    e_mail=models.EmailField(max_length=254)
    cel=models.IntegerField()
    foto=models.ImageField(upload_to='imagenes', null=True, blank = True)
    
    def __str__(self):
        return f" {self.nombre} - {self.apellido} - {self.edad} - {self.localidad} - {self.e_mail} - {self.cel} - {self.foto}"


