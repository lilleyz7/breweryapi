# Generated by Django 5.1.2 on 2024-10-15 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brew_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('url', models.URLField(max_length=100)),
                ('saved_by_users', models.ManyToManyField(blank=True, related_name='saved_breweries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
