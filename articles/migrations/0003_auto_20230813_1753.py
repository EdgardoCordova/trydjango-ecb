# Generated by Django 3.2.20 on 2023-08-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230812_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sum',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='valor1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='valor2',
            field=models.TextField(null=True),
        ),
    ]
