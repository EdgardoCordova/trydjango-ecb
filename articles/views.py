from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template.loader import render_to_string
from .forms import ArticleForm
#from datetime import datetime


# Create your views here.

# esta vista utilizando un formulario

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    
    context = {
        'form': form
    }

    def actualizar_suma(article_id, valor):
        try:
            article_obj = Article.objects.get(id=article_id)
            article_obj.suma = valor
            article_obj.save()
            print(f"Actualización exitosa para Article {article_id}")
        except KeyError:
            print(f"No se encontró Article con ID {article_id}")

    # a continuacion se habilitara, si se completo el formulario    
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()

        valor1 = form.cleaned_data.get('valor1')        
        valor2 = form.cleaned_data.get('valor2')
        suma = int(valor1) + int(valor2)

        article_qs = Article.objects.all()
        context = {
        'object_list': article_qs
        }
        
        actualizar_suma(article_object.id, suma)  # Aquí estaba article_id, debe ser article_object.id


        return render(request, 'home_view.html', context=context)    
    
    #print(hora, "views: def article_create_view: form no valido")        
    return render(request, 'articles/create.html', context=context)
"""
opcion 2
@login_required
def article_create_view(request):    
    #print(request.POST)
    form = ArticleForm()
    print(dir(form))
    context = {
        'form': form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            def actualizacion(self, article_id, valor):
    try:
        article_obj = self[article_id]
        article_obj.suma = valor
        article_obj.save()
        print(f"Actualización exitosa para Article {article_id}")
    except KeyError:
        print(f"No se encontró Article con ID {article_id}")

            content = form.cleaned_data.get('content')
            #print(title,content)
            article_object = Article.objects.create(title=title, content=content)
            context['object'] = article_object
            context['created'] = True
    return render(request, 'articles/create.html', context=context)
"""
"""
opcion 1
@login_required
def article_create_view(request):    
    #print(request.POST)
    context = {}
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title,content)
        article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request, 'articles/create.html', context=context)
"""
def article_search_view(request):
    #print(dir(request))
    #print(request.path)
    
    query_dict = request.GET  # this is a dictionary
    query = query_dict.get('q')  # la 'q' viene de base.html: <input type="text" name="q"/>
    
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context={
        'object': article_obj
    }
    return render(request, 'articles/search.html', context=context)


def article_detail_view(request, id=None):
    #now = datetime.now()
    #hora = now.strftime('%H:%M:%S')
    #print(hora, 'views: def article_detail_view')
    article_obj = None
    if id is not None: 
        article_obj = Article.objects.get(id=id)
    context = {
        'object': article_obj,
    }
    return render(request, 'articles/detail.html', context=context)
    
