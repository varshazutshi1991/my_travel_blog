# Generated by Django 2.0.7 on 2018-07-19 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180719_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='travel_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='blog',
            name='travel_images',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
