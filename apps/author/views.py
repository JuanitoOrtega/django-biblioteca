from django.shortcuts import render
from django.views.generic import ListView
from .models import Author


class ListAuthors(ListView):
    # model = Author # Cuando se usa una petición personalizada con get_queryset no es necesario
    template_name = 'author/list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')

        return Author.objects.buscar_autor4(palabra_clave)