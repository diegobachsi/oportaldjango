# Generated by Django 3.2.6 on 2021-08-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título Vídeo')),
                ('slug', models.SlugField(unique=True, verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição Simples')),
                ('watched_at', models.DateTimeField(auto_now_add=True, verbose_name='Assistido em:')),
            ],
            options={
                'verbose_name': 'Videos',
                'verbose_name_plural': 'Videos',
                'ordering': ['title'],
            },
        ),
    ]
