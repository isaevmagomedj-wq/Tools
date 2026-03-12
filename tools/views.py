from rest_framework import generics, permissions

from .models import Category, Tools, FeedBack
from .permissions import IsAuthorOrReadOnly
from .serializers import CategorySerializer, ToolsSerializer, FeedBackSerializer


class CategoryList(generics.ListCreateAPIView):
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
