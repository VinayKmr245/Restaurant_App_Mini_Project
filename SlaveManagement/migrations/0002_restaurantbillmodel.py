# Generated by Django 2.0.13 on 2020-10-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlaveManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantBillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('noofchairs', models.CharField(max_length=100)),
                ('itemcodes', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('totalamount', models.FloatField()),
                ('branchUser', models.CharField(max_length=100)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'BillTable',
            },
        ),
    ]
