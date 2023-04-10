from django import forms

class RegistradoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    localidad=forms.CharField(max_length=20)
    e_mail=forms.EmailField(max_length=254)
    cel=forms.IntegerField()
    foto=forms.ImageField()
    