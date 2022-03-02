# Generated by Django 3.2.9 on 2022-02-09 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0002_weatheroptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.location'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.location'),
        ),
    ]