# Generated by Django 3.1.7 on 2021-03-14 21:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210314_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 14, 21, 49, 17, 327556, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 14, 21, 49, 17, 325937, tzinfo=utc)),
        ),
    ]
