from django.urls import path
from .views import *


urlpatterns = [
    path('books/create/', create_book, name='book-create'),
    path('books/', books, name='book-list'),
    path('books/<str:pk>/', book, name='book-detail'),
    path('books/<str:pk>/update/', update_book, name='book-update'),
    path('books/<str:pk>/delete/', delete_book, name='book-delete'),
]




