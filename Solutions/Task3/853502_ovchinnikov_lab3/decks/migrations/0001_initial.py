# Generated by Django 3.0.6 on 2020-05-15 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arthetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Архетип')),
                ('winrate', models.SmallIntegerField(verbose_name='Процент побед')),
                ('best_matchup', models.CharField(max_length=100, verbose_name='Лучший противник')),
                ('worst_matchup', models.CharField(max_length=100, verbose_name='Худший противник')),
            ],
            options={
                'verbose_name': 'Архетип',
                'verbose_name_plural': 'Архетипы',
            },
        ),
        migrations.CreateModel(
            name='Deck_Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='deck_picture/', verbose_name='Скриншот колоды')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Изображение класса',
                'verbose_name_plural': 'Изображения классов',
            },
        ),
        migrations.CreateModel(
            name='Deck_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Описание колоды')),
                ('rating', models.SmallIntegerField(verbose_name='Оценка')),
                ('comment', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опсание колоды',
                'verbose_name_plural': 'Описания колод',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя игрока')),
                ('player_nickname', models.CharField(max_length=100, verbose_name='Никнейми игрока')),
                ('rank', models.CharField(max_length=100, verbose_name='Ранк игрока')),
                ('prizes', models.TextField(verbose_name='Награды')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Колода')),
                ('deck_tier', models.CharField(default='D', max_length=100, verbose_name='Тир колоды')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('image', models.ImageField(upload_to='deck/', verbose_name='Изображение')),
                ('archetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Arthetype', verbose_name='Архетип')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Player', verbose_name='Игрок')),
                ('review', models.ForeignKey(default='Пусто', on_delete=django.db.models.deletion.CASCADE, to='decks.Deck_Review', verbose_name='Опсание колоды')),
            ],
            options={
                'verbose_name': 'Колода',
                'verbose_name_plural': 'Колоды',
            },
        ),
    ]
