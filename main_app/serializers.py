from django.contrib.auth.models import Group, User
from .models import Recipe, Ingredient, RecipeIngredient
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientsSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class RecipesSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'author', 'created_at', 'updated_at', 'ingredients']