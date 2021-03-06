# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-15 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('ssn', models.IntegerField()),
                ('lang', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BloodWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BloodWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WBC', 'WBC'), ('ANC', 'ANC'), ('Hemoglobin', 'Hemo'), ('Platlets', 'Platlets'), ('Calcium', 'Calcium')], default='WBC', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('dateadded', models.DateField()),
                ('dateupdated', models.DateField()),
                ('dosage', models.CharField(max_length=128)),
                ('frequency', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_visit', models.CharField(choices=[('Hospital', 'Hospital'), ('Home', 'Home')], default='Hospital', max_length=32)),
                ('date', models.DateTimeField()),
                ('reason_for_visit', models.TextField()),
                ('bloodwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.BloodWork')),
                ('medications', models.ManyToManyField(to='dashboard.Medication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.AccountInfo')),
            ],
        ),
        migrations.AddField(
            model_name='bloodwork',
            name='type',
            field=models.ManyToManyField(to='dashboard.BloodWorkType'),
        ),
    ]
