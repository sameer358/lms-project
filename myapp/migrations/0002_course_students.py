# Generated by Django 5.0.3 on 2024-04-17 18:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
    ]