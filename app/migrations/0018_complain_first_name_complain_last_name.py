# Generated by Django 4.1.3 on 2022-12-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_admin_adminid_admin_gender_technician_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='complain',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]