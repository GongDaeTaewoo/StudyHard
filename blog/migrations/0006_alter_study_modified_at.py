# Generated by Django 4.2.5 on 2023-09-30 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_study_repeat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='modified_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
