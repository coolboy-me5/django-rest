# Generated by Django 5.0.6 on 2024-06-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
