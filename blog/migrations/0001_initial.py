# Generated by Django 2.0.7 on 2018-07-17 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('travel_place', models.CharField(max_length=100)),
                ('travel_date', models.DateField(auto_now=True)),
                ('travel_story', models.TextField()),
                ('travel_images', models.ImageField(height_field=100, upload_to='', width_field=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogger'),
        ),
    ]
