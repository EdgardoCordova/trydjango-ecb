# this renders html web pages
from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string


def home_view(request):
    # Take in a request (django sends request)
    # Return HTML as a response (we pick to return the response)
    # name = ""
    random_id = random.randint(1,4) # API call to some rest API with Python and Python request
    article_obj = Article.objects.get(id=random_id)
    article_qs = Article.objects.all()
    my_list = [102,34,345,99,123]
    
    context={
        'my_list': my_list,
        'object': article_obj,
        'title': article_obj.title,
        'content': article_obj.content,
        'object_list': article_qs
    }

    HTML_STRING = render_to_string('home_view.html', context=context)

    return HttpResponse(HTML_STRING)


