# Generated by Django 3.2.13 on 2022-10-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
