# Generated by Django 3.1.7 on 2021-02-27 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0006_csv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Csv',
            new_name='Pickle',
        ),
    ]
