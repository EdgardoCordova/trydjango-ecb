from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.TextField(null=True)
    content = models.TextField(null=True)
    valor1 = models.IntegerField(null=True)
    valor2 = models.IntegerField(null=True)
    suma = models.IntegerField(null=True)

    def __str__(self):
        print('models.py: classArticle()')
        return str(self.id)
