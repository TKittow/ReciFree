from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes', blank=True)

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