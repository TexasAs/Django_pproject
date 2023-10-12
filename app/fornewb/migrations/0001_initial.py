# Generated by Django 4.2.5 on 2023-10-02 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Уровень')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровни сложности',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Fornewb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=255, verbose_name='Название статьи')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='article_image/%Y/%m/%d')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликована ли')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fornewb.category')),
            ],
            options={
                'verbose_name': 'Статьи для новичков программистов',
                'verbose_name_plural': 'Статьи для новичков программистов',
                'ordering': ['-time_create', 'article_title'],
            },
        ),
    ]