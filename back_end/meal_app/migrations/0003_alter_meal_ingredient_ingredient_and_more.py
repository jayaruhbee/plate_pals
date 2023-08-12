# Generated by Django 4.2.4 on 2023-08-12 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0002_remove_ingredient_meal_meal_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal_ingredient',
            name='ingredient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meal_app.ingredient'),
        ),
        migrations.AlterField(
            model_name='meal_ingredient',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_ingredients', to='meal_app.meal'),
        ),
    ]