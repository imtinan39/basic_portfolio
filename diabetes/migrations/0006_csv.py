# Generated by Django 3.1.7 on 2021-02-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0005_auto_20210227_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to='')),
            ],
        ),
    ]
