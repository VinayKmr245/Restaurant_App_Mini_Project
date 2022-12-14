# Generated by Django 2.0.13 on 2020-10-14 13:26

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantInformation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='branchuserregistermodel',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='branchuserregistermodel',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='branchuserregistermodel',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
