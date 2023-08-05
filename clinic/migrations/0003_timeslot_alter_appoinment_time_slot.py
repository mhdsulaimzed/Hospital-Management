# Generated by Django 4.2.3 on 2023-08-04 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_appoinment_alter_doctor_department_delete_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.doctor')),
            ],
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='time_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.timeslot'),
        ),
    ]