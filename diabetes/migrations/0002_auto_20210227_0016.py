# Generated by Django 3.1.7 on 2021-02-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
