# Generated by Django 4.1.3 on 2022-11-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_person_first_name_remove_person_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=100, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=100, max_length=30),
            preserve_default=False,
        ),
    ]
