# Generated by Django 4.2.10 on 2024-04-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_alter_apimeal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimeal',
            name='steps',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]