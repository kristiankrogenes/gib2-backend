# Generated by Django 3.2.12 on 2022-02-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_gasstation'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasstation',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]