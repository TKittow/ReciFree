from .models import Recipe, Ingredient, ApiMeal
from rest_framework import permissions, viewsets, status, parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.decorators.csrf import csrf_exempt

from .serializers import *

from django.contrib.auth.models import Group, User
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import api_view
import uuid
import os

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def userFinder(request):
    user = request.data.get('username')
    return User.objects.get(username=user)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})  # Pass request to serializer context
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Create RecipeIngredient instances for each ingredient
        recipe = serializer.instance
        ingredients_data = request.data.get('ingredients', [])
        for ingredient_data in ingredients_data:
            ingredient_id = ingredient_data.get('id')
            quantity = ingredient_data.get('quantity')
            RecipeIngredient.objects.create(recipe=recipe, ingredient_id=ingredient_id, quantity=quantity)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get(self, request):
        serializer = RecipesSerializer(Recipe.objects.all(), many=True, context={'request': request})  # Pass request to serializer context
        return Response(data=serializer.data)

        

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [permissions.IsAuthenticated]

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserDetailView(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, context={'request': request})  # Pass request to serializer context
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        
class ApiMealViewSet(viewsets.ModelViewSet):
    queryset = ApiMeal.objects.all()
    serializer_class = ApiMealsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})  # Pass request to serializer context
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        serializer = ApiMealsSerializer(ApiMeal.objects.all(), many=True, context={'request': request})  # Pass request to serializer context
        return Response(data=serializer.data)

class MealsUserAdded(APIView):
    def get(self, request, username):
        # Filter meals based on the provided username
        meals = ApiMeal.objects.filter(author=username)
        serializer = ApiMealsSerializer(meals, many=True)
        return Response(serializer.data)