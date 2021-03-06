# Generated by Django 2.2.11 on 2020-03-14 19:37

from django.db import migrations, models
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_carouseldesktop'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCaption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HomePictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('picture', imagekit.models.fields.ProcessedImageField(upload_to='homepictures_desktop')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
