# Generated by Django 4.1.4 on 2022-12-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_alter_whogetoffer_email_alter_whogetoffer_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whogetoffer',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='whogetoffer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]