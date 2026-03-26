from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Category, Tools, FeedBack
from .permissions import IsAuthorOrReadOnly
from .serializers import CategorySerializer, ToolsSerializer, FeedBackSerializer, UserSerializer


'''class CategoryList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ToolsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

class ToolsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

class FeedBackList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

class FeedBackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer'''

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ToolsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

class FeedBackViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer