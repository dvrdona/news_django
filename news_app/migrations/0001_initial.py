# Generated by Django 5.1.1 on 2024-09-12 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('main_text', models.TextField(max_length=256)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('cotegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.newscategory')),
            ],
        ),
    ]
