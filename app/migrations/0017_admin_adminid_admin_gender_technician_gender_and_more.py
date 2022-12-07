# Generated by Django 4.1.3 on 2022-12-05 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_maintenance_room_alter_maintenance_studentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='adminID',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='gender',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='technician',
            name='gender',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='technician',
            name='technicianID',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]