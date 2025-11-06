from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'descricao', 'categoria', 'imagem', 'arquivo']

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields['imagem'].required = False
        self.fields['arquivo'].required = False