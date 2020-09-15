# Generated by Django 2.1.7 on 2019-03-06 08:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20190306_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 17, 3, 639571, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Reason',
            field=models.ForeignKey(default='Expenditure Reason', on_delete=django.db.models.deletion.CASCADE, to='dashboard.Spend'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 17, 3, 638169, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 17, 3, 639571, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 17, 3, 639167, tzinfo=utc)),
        ),
    ]