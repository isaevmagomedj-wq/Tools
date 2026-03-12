from rest_framework import generics 

from .models import Category, Tools, FeedBack
from .serializers import CategorySerializer, ToolsSerializer, FeedBackSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ToolsList(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

class ToolsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer

class FeedBackList(generics.ListCreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

class FeedBackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
