# Generated by Django 3.2.12 on 2022-03-09 13:56

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.PositiveIntegerField(blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, default='POINT(0.0 0.0)', srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, default='POINT(0.0 0.0)', srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('geom', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('diesel', models.FloatField(blank=True)),
                ('unleaded', models.FloatField(blank=True)),
                ('electric', models.FloatField(blank=True)),
                ('gas_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gasstation')),
            ],
        ),
    ]
