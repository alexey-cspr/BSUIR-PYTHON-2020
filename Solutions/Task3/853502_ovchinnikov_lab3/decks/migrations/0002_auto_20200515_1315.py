# Generated by Django 3.0.6 on 2020-05-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='url',
            field=models.CharField(max_length=100, verbose_name='Ссылка на видео'),
        ),
    ]
