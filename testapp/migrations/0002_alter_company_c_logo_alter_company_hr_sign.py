# Generated by Django 4.0.6 on 2022-08-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='c_logo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='hr_sign',
            field=models.ImageField(upload_to=''),
        ),
    ]
