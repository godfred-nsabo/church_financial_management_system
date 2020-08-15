# Generated by Django 2.1.5 on 2019-02-21 06:42

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0006_auto_20190221_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='Figures',
        ),
        migrations.RemoveField(
            model_name='spend',
            name='Figures',
        ),
        migrations.RemoveField(
            model_name='sundry',
            name='Figures',
        ),
        migrations.AddField(
            model_name='salary',
            name='AmountInWords',
            field=models.TextField(default='amount in words', max_length=500),
        ),
        migrations.AddField(
            model_name='spend',
            name='AmountInWords',
            field=models.TextField(default='amount in words', max_length=500),
        ),
        migrations.AddField(
            model_name='sundry',
            name='AmountInWords',
            field=models.TextField(default='amount in words', max_length=500),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 2, 21, 6, 42, 11, 26848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 2, 21, 6, 42, 11, 27845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 2, 21, 6, 42, 11, 27845, tzinfo=utc)),
        ),
    ]
