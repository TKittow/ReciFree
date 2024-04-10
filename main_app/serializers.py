from django.contrib.auth.models import Group, User
from .models import Recipe, Ingredient, RecipeIngredient, ApiMeal
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

    def __str__(self):
        return self.username

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
    ingredient1 = IngredientsSerializer(many=False, read_only=True)
    ingredient2 = IngredientsSerializer(many=False, read_only=True)
    ingredient3 = IngredientsSerializer(many=False, read_only=True)
    ingredient4 = IngredientsSerializer(many=False, read_only=True)
    ingredient5 = IngredientsSerializer(many=False, read_only=True)
    ingredient6 = IngredientsSerializer(many=False, read_only=True)
    ingredient7 = IngredientsSerializer(many=False, read_only=True)
    ingredient8 = IngredientsSerializer(many=False, read_only=True)
    ingredient9 = IngredientsSerializer(many=False, read_only=True)
    ingredient10 = IngredientsSerializer(many=False, read_only=True)
    ingredient11 = IngredientsSerializer(many=False, read_only=True)
    ingredient12 = IngredientsSerializer(many=False, read_only=True)
    ingredient12 = IngredientsSerializer(many=False, read_only=True)
    ingredient13 = IngredientsSerializer(many=False, read_only=True)
    ingredient14 = IngredientsSerializer(many=False, read_only=True)
    ingredient15 = IngredientsSerializer(many=False, read_only=True)
    ingredient16 = IngredientsSerializer(many=False, read_only=True)
    ingredient17 = IngredientsSerializer(many=False, read_only=True)
    ingredient18 = IngredientsSerializer(many=False, read_only=True)
    ingredient19 = IngredientsSerializer(many=False, read_only=True)
    ingredient20 = IngredientsSerializer(many=False, read_only=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'author', 'created_at', 'updated_at', 'image', 'ingredient1',
                'ingredient2',
                'ingredient3',
                'ingredient4',
                'ingredient5',
                'ingredient6',
                'ingredient7',
                'ingredient8',
                'ingredient9',
                'ingredient10',
                'ingredient11',
                'ingredient12',
                'ingredient13',
                'ingredient14',
                'ingredient15',
                'ingredient16',
                'ingredient17',
                'ingredient18',
                'ingredient19',
                'ingredient20',
                'measurement1',
                'measurement2',
                'measurement3',
                'measurement4',
                'measurement5',
                'measurement6',
                'measurement7',
                'measurement8',
                'measurement9',
                'measurement10',
                'measurement11',
                'measurement12',
                'measurement13',
                'measurement14',
                'measurement15',
                'measurement16',
                'measurement17',
                'measurement18',
                'measurement19',
                'measurement20',]
    
    def get_author(self, obj):
        return {'username': 'Test'}
         
class ApiMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiMeal
        fields = ['id', 'name', 'api_id', 'description', 'source', 'created_at', 'updated_at', 'steps', 'image']
    
