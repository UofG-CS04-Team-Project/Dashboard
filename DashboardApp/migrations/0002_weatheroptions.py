# Generated by Django 3.2.9 on 2022-02-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
