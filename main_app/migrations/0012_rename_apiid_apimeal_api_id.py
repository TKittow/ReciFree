# Generated by Django 4.2.10 on 2024-04-09 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_apimeal_remove_recipe_api'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apimeal',
            old_name='apiId',
            new_name='api_id',
        ),
    ]
