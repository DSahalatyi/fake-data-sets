# Generated by Django 5.1.4 on 2024-12-18 13:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schemas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schemas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='column',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='schemas.schema'),
        ),
    ]
