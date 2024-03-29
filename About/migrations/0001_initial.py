# Generated by Django 5.0.3 on 2024-03-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About_model/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='About_spering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About_spering/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'About_spering',
                'verbose_name_plural': 'Abouts_spering',
            },
        ),
    ]
