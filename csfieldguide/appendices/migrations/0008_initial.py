# Generated by Django 4.2.9 on 2024-02-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appendices', '0007_auto_20190209_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppendixPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('template', models.CharField(max_length=100)),
                ('url_name', models.CharField(max_length=100)),
            ],
        ),
    ]
