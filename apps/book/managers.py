import datetime
from django.db import models
from django.db.models import Count


class BookManager(models.Manager):
    """ managers para el modelo book """

    def list_books(self, kword):
        # resultado = self.filter(title__icontains=kword, published__range=('1985-01-01', '2011-12-12'))
        resultado = self.filter(title__icontains=kword)
        return resultado

    def list_books2(self, kword, fecha1, fecha2):
        # Si hubiera error en el formato de la fecha
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        resultado = self.filter(title__icontains=kword, published__range=(date1, date2))
        return resultado

    def list_books_category(self, category):
        return self.filter(category__id=category).order_by('title')

    def add_author_book(self, book_id, author):
        book = self.get(id=book_id)
        book.authors.add(author)
        return book

    def books_num_lends(self):
        result = self.aggregate(num_lends=Count('book_lend')) # Aggregate devuelve un diccionario
        return result


class CategoryManager(models.Manager):
    """ managers para el modelo category """

    def category_by_author(self, author):
        return self.filter(category_book__authors__id=author).distinct() # para no repetir las consultas

    def list_category_books(self):
        result = self.annotate(num_books=Count('category_book'))

        for r in result:
            print('***************')
            print(r, r.num_books)

        return result