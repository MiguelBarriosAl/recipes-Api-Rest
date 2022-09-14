# Generated by Django 4.1.1 on 2022-09-14 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_recipe_ingredients_remove_recipe_recipe_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_steps',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='labels',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
