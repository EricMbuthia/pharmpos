# Generated by Django 3.2.4 on 2021-08-27 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210826_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date_time_entered',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 6, 33, 53, 138642, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('product', 'store')},
        ),
    ]
