# Generated by Django 4.1.1 on 2022-09-13 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_recipe_ingredients_alter_recipe_labels_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_steps',
        ),
    ]
