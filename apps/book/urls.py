from django.urls import path
from .views import *


urlpatterns = [
    path('books/', ListBooks.as_view(), name='list_books'),
]