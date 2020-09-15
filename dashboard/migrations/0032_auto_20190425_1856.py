# Generated by Django 2.1.7 on 2019-04-25 15:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_auto_20190425_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 544067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offerings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 540092, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offerings',
            name='DayOfTheWeek',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pledges',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 542194, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pledges',
            name='DayOfTheWeek',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 538501, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salaryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 544991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 543038, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 540092, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 544067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tithes',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 4, 25, 15, 56, 4, 541047, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tithes',
            name='DayOfTheWeek',
            field=models.CharField(max_length=100),
        ),
    ]