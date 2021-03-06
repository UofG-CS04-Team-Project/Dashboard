# Generated by Django 3.2.9 on 2022-02-03 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(max_length=64)),
                ('serial', models.CharField(max_length=64)),
                ('kind', models.CharField(choices=[('Camera', 'Cam'), ('Environmental', 'Env')], max_length=13)),
                ('description', models.TextField(blank=True)),
                ('interval', models.IntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.location')),
            ],
            options={
                'unique_together': {('org_id', 'serial')},
            },
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('Temperature', 'Tm'), ('Humidity', 'Hd'), ('Occupancy', 'Oc')], max_length=11)),
                ('tstamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.location')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.sensor')),
            ],
        ),
    ]
