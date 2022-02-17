# Generated by Django 3.2.12 on 2022-02-17 13:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_currentposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
    ]
