# Generated by Django 4.2.3 on 2023-08-04 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_timeslot_alter_appoinment_time_slot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='doctor',
        ),
    ]