# Generated by Django 4.2.4 on 2023-08-12 20:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan_app', '0002_remove_meal_plan_friday_remove_meal_plan_monday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.date(2023, 8, 12)),
        ),
        migrations.AlterField(
            model_name='day',
            name='meal_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days_of_meals', to='meal_plan_app.meal_plan'),
        ),
    ]