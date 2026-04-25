from django import forms
from .models import Cliente


class Form(forms.Form):
    model = Cliente

    fields = ['nome', 'email', 'mensagem']
