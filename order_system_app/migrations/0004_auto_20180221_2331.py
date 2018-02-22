# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-21 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_system_app', '0003_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='meals_images/')),
                ('price', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_system_app.Restaurant')),
            ],
        ),
        migrations.RemoveField(
            model_name='meal',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
    ]