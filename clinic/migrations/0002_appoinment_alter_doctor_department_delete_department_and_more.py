# Generated by Django 4.2.3 on 2023-08-04 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('status', models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending')], default='pending', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Neurology', 'Neurology'), ('General Medicine', 'General Medicine'), ('Ortho', 'Ortho')], default='General Medicicne', max_length=200),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.AddField(
            model_name='appoinment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.doctor'),
        ),
        migrations.AddField(
            model_name='appoinment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
