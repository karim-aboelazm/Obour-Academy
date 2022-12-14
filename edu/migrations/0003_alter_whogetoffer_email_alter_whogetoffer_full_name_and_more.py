# Generated by Django 4.1.4 on 2022-12-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_whogetoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whogetoffer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='whogetoffer',
            name='full_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='whogetoffer',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
