from django.contrib.auth.models import Group, User
from .models import Recipe, Ingredient, RecipeIngredient, ApiMeal
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

    def __str__(self):
        return self

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ['recipe','ingredient', 'measurement']

class RecipesSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'author', 'created_at', 'updated_at', 'image', 'ingredients', 'steps']
         
class ApiMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiMeal
        fields = ['id', 'name', 'api_id', 'description', 'source', 'created_at', 'updated_at', 'steps', 'image']
    
