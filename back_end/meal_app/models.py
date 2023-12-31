from django.db import models

class Meal(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to='meal_images/', blank = True, null = True)
    image_url = models.TextField(blank = True, null = True)
    category = models.CharField()
    instructions = models.TextField(blank = True, null = True)
    ingredients = models.TextField(blank = True, null = True)
    notes = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"Title: {self.title}, Category: {self.category}, Instructions: {self.instructions}"


class Ingredient(models.Model):
    title = models.CharField()
    measurement = models.CharField()

    def __str__(self):
        return f"Title: {self.title}, Measurement: {self.measurement}"


class Meal_ingredient(models.Model):
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='meal_ingredients')
    ingredient = models.OneToOneField(
        Ingredient, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Meal: {self.meal}, Ingredient: {self.ingredient}"
