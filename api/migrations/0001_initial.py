# Generated by Django 3.2.12 on 2022-04-25 09:24

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
            name='County',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('brand', models.CharField(blank=True, max_length=30, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326)),
                ('county', models.CharField(blank=True, default='Ukjent', max_length=30, null=True)),
                ('municipality', models.CharField(blank=True, default='Ukjent', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('diesel', models.FloatField(blank=True)),
                ('octane_95', models.FloatField(blank=True)),
                ('electric', models.FloatField(blank=True)),
                ('gas_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gasstation')),
            ],
        ),
    ]
