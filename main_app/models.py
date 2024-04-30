from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed (e.g., nutritional information)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100, null=False, default='Unidentified')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    #Steps
    steps = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} ({self.recipe.name})"
    
class ApiMeal(models.Model):
    name = models.CharField(max_length=200)
    api_id = models.CharField(max_length=20)
    description = models.TextField()
    source = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.TextField(max_length=300)
    steps = models.TextField(max_length=3000, null=True)
    author = models.CharField(max_length=100, null=False, default='Unidentified')

    def __str__(self):
        return self.name