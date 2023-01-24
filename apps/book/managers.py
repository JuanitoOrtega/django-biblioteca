from django.db import models


class BookManager(models.Manager):
    """ managers para el modelo book """

    def list_books(self, kword):
        resultado = self.filter(title__icontains=kword, published__range=('1985-01-01', '2011-12-12'))
        return resultado