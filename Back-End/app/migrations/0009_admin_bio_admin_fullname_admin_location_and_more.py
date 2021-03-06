# Generated by Django 4.0.5 on 2022-07-06 08:48

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_intervention_user_alter_redflag_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='bio',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='fullname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='organisation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png', max_length=255),
        ),
        migrations.AddField(
            model_name='client',
            name='bio',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='fullname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='organisation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png', max_length=255),
        ),
    ]
