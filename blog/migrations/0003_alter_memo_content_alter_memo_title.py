# Generated by Django 4.2.5 on 2023-09-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_study_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='content',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='memo',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]