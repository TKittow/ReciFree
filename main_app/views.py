from .models import Recipe, Ingredient
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

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import api_view
import uuid
import os
# import boto3

from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def userFinder(request):
    user = request.data.get('username')
    return User.objects.get(username = user)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def create_recipe(request, *args, **kwargs):
        print(request)
        post_id = kwargs.get('pk')
        user_id = request.user.id
        user = User.objects.get(id=user_id)  
        post = Post.objects.get(pk=post_id)
        comment_text = request.data.get('comment_text')
        comment = Comment.objects.create(post=post, comment_text=comment_text, user=user)
        return Response({'message': 'Comment created successfully'})

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