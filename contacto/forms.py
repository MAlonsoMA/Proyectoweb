from django import forms


class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)
    email=forms.EmailField(label="Email",required=True)
    contenido=forms.CharField(label="Contenido",required=False,widget=forms.Textarea)
    
    nombre.widget.attrs.update({"class": "form-control mb-2"})
    email.widget.attrs.update({"class": "form-control mb-2"})
    contenido.widget.attrs.update({"class": "form-control","rows": 5,"cols": 50})
