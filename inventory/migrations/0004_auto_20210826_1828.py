# Generated by Django 3.2.4 on 2021-08-26 15:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210826_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='date_time_entered',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 15, 28, 14, 992905, tzinfo=utc)),
        ),
    ]
