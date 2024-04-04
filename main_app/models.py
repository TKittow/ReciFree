from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.TextField()

    # Ingredients
    ingredient1 = models.CharField(max_length=100, blank=True, null=True)
    ingredient2 = models.CharField(max_length=100, blank=True, null=True)
    ingredient3 = models.CharField(max_length=100, blank=True, null=True)
    ingredient4 = models.CharField(max_length=100, blank=True, null=True)
    ingredient5 = models.CharField(max_length=100, blank=True, null=True)
    ingredient6 = models.CharField(max_length=100, blank=True, null=True)
    ingredient7 = models.CharField(max_length=100, blank=True, null=True)
    ingredient8 = models.CharField(max_length=100, blank=True, null=True)
    ingredient9 = models.CharField(max_length=100, blank=True, null=True)
    ingredient10 = models.CharField(max_length=100, blank=True, null=True)
    ingredient11 = models.CharField(max_length=100, blank=True, null=True)
    ingredient12 = models.CharField(max_length=100, blank=True, null=True)
    ingredient13 = models.CharField(max_length=100, blank=True, null=True)
    ingredient14 = models.CharField(max_length=100, blank=True, null=True)
    ingredient15 = models.CharField(max_length=100, blank=True, null=True)
    ingredient16 = models.CharField(max_length=100, blank=True, null=True)
    ingredient17 = models.CharField(max_length=100, blank=True, null=True)
    ingredient18 = models.CharField(max_length=100, blank=True, null=True)
    ingredient19 = models.CharField(max_length=100, blank=True, null=True)
    ingredient20 = models.CharField(max_length=100, blank=True, null=True)

    # Measurements
    measurement1 = models.CharField(max_length=100, blank=True, null=True)
    measurement2 = models.CharField(max_length=100, blank=True, null=True)
    measurement3 = models.CharField(max_length=100, blank=True, null=True)
    measurement4 = models.CharField(max_length=100, blank=True, null=True)
    measurement5 = models.CharField(max_length=100, blank=True, null=True)
    measurement6 = models.CharField(max_length=100, blank=True, null=True)
    measurement7 = models.CharField(max_length=100, blank=True, null=True)
    measurement8 = models.CharField(max_length=100, blank=True, null=True)
    measurement9 = models.CharField(max_length=100, blank=True, null=True)
    measurement10 = models.CharField(max_length=100, blank=True, null=True)
    measurement11 = models.CharField(max_length=100, blank=True, null=True)
    measurement12 = models.CharField(max_length=100, blank=True, null=True)
    measurement13 = models.CharField(max_length=100, blank=True, null=True)
    measurement14 = models.CharField(max_length=100, blank=True, null=True)
    measurement15 = models.CharField(max_length=100, blank=True, null=True)
    measurement16 = models.CharField(max_length=100, blank=True, null=True)
    measurement17 = models.CharField(max_length=100, blank=True, null=True)
    measurement18 = models.CharField(max_length=100, blank=True, null=True)
    measurement19 = models.CharField(max_length=100, blank=True, null=True)
    measurement20 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Add more fields as needed (e.g., nutritional information)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} ({self.recipe.name})"