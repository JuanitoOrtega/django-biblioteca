from django.views.generic import ListView, DetailView
from .models import Book


class ListBooks(ListView):
    context_object_name = 'books'
    template_name = 'book/list.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')

        # Fecha 1
        f1 = self.request.GET.get('fecha1', '')
        # Fecha 2
        f2 = self.request.GET.get('fecha2', '')

        if f1 and f2:
            return Book.objects.list_books2(palabra_clave, f1, f2)
        else:
            return Book.objects.list_books(palabra_clave)


class ListBooks2(ListView):
    context_object_name = 'books'
    template_name = 'book/list2.html'

    def get_queryset(self):
        return Book.objects.list_books_category('1')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'