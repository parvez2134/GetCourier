# Generated by Django 3.1.5 on 2021-04-19 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20210318_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_requirement',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 19, 10, 57, 3, 915756)),
        ),
    ]
