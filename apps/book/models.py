from django.db import models
from apps.author.models import Author


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre de categoría')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    authors = models.ManyToManyField(Author, verbose_name='Autores')
    title = models.CharField(max_length=100, unique=True, verbose_name='Título del libro')
    published = models.DateField(blank=True, null=True, verbose_name='Lanzamiento')
    image = models.ImageField(blank=True, null=True, upload_to='books', verbose_name='Portada')
    views = models.PositiveIntegerField(default=0, verbose_name='Visitas')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.title