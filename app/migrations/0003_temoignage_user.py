# Generated by Django 4.2.11 on 2024-05-03 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_find_adresse_remove_find_arrondissement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temoignage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
