# Generated by Django 4.0.5 on 2022-07-04 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_redflag_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redflag',
            name='stages',
            field=models.CharField(choices=[('investigation', 'investigation'), ('rejected', 'rejected'), ('resolved', 'resolved')], default='', max_length=20, null=True),
        ),
    ]