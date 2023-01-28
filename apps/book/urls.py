from django.urls import path
from .views import *


urlpatterns = [
    path('books/', ListBooks.as_view(), name='list_books'),
    path('books2/', ListBooks2.as_view(), name='list_books2'),
    path('books/<pk>/', BookDetailView.as_view(), name='detail_book'),
]