from django.views.generic import ListView
from .models import Book


class ListBooks(ListView):
    context_object_name = 'books'
    template_name = 'book/list.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        return Book.objects.list_books(palabra_clave)
    