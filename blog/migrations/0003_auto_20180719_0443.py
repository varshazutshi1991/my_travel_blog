# Generated by Django 2.0.7 on 2018-07-19 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_travel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='travel_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 18, 4, 43, 27, 172686)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='travel_images',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
