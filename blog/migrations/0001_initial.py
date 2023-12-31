# Generated by Django 4.2.5 on 2023-09-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=15)),
                ('address', models.URLField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=15)),
                ('content', models.TextField(max_length=1000)),
                ('level', models.PositiveSmallIntegerField()),
                ('importance', models.PositiveSmallIntegerField()),
                ('repeat', models.PositiveSmallIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField()),
            ],
        ),
    ]
