# Generated by Django 3.0.6 on 2020-05-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecraft', '0004_auto_20200513_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverfeature',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serverrule',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
