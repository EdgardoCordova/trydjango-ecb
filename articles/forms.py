from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'valor1', 'valor2']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        #qs = Article.objects.filter(title__icontains=title)   # le quitamos el all()
        qs = Article.objects.filter(title__icontains='fuck')   # le quitamos el all()
        if qs.exists():
            self.add_error('title', f'\'{title}\' is already in use, pick another title')
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    valor1 = forms.IntegerField()
    valor2 = forms.IntegerField()
    sum = forms.IntegerField()



    """
    def clean_title(self):
        cleaned_data = self.cleaned_data  # dictionary
        title = cleaned_data.get('title')
        if title.lower().strip() == 'prohibido':
            raise forms.ValidationError('this title is forbidden') 
        return title
    """
    # esta funcion nunca se ejecuta
    def calculo(self):
        print('forms.py, class ArticleForm, def calculo(self), calculo ')
    
    # esta funcion se ejecuta luego de completar el formulario, pero no se graba. solo sirve para verificacion
    def clean(self):
        now = datetime.now()
        hora = now.strftime('%H:%M:%S')
        cleaned_data = self.cleaned_data 
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        valor1 = cleaned_data.get('valor1')
        valor2 = cleaned_data.get('valor2')
        calculo = valor1 * valor2
        print(hora, 'forms.py, class ArticleForm, def clean(self), multiplicacion ', calculo)

        if title.lower().strip() == 'prohibido':
            self.add_error('title', 'this title is forbidden')
        if 'xxx' in content or 'xxx' in title:
            raise forms.ValidationError('XXX ...not allowed') 
        return cleaned_data # cleaned_data es un diccionario
    