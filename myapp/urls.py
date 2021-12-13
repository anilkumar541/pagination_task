from django.urls import path
from myapp import views


urlpatterns = [
    path("quote_api/", views.QuoteListCreateView.as_view()),
    path("quote_api/<int:pk>/", views.QuoteRUDView.as_view()),
    path("category_api/", views.CategoryListCreateView.as_view()),
    path("category_api/<int:pk>/", views.CategoryRUDView.as_view()),
    

]
