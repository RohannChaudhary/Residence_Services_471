# Generated by Django 4.1.3 on 2022-11-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_person_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
