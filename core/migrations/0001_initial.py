# Generated by Django 4.1.2 on 2022-10-16 09:20

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
                ('meta_text', models.TextField(max_length=300)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('published', models.BooleanField(default=False)),
                ('slider', models.BooleanField(default=False)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('comment', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '2. Posts',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': '1. Category',
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 10, 16, 9, 20, 52, 634735))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3. Comments',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='core.category'),
        ),
    ]
