# Generated by Django 4.2.10 on 2024-04-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_rename_apiid_apimeal_api_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='apimeal',
            name='steps',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeal',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]