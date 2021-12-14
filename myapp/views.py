from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from myapp.models import Quote, Category
from myapp.serializers import QuoteSerializer, CategorySerializer
# from rest_framework.pagination import PageNumberPagination
from myapp.pagination import MyPageNumberPagination, TestLimitOffsetPagination, TestCursorPagination


class QuoteListCreateView(ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    # pagination_class = MyPageNumberPagination
    # pagination_class =TestLimitOffsetPagination
    pagination_class = TestCursorPagination


class QuoteRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    #  pagination_class = MyPageNumberPagination

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #  pagination_class = MyPageNumberPagination
    

class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #  pagination_class = MyPageNumberPagination
        

