from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from myapp.models import Quote, Category
from myapp.serializers import QuoteSerializer, CategorySerializer
# from rest_framework.pagination import PageNumberPagination
from myapp.pagination import MyPageNumberPagination


class QuoteListCreateView(ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    pagination_class = MyPageNumberPagination

class QuoteRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
        

