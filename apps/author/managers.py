from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):
    """ managers para el modelo author """

    # def buscar_autor(self, kword):
    #     resultado = self.filter(first_name__icontains=kword)
    #     return resultado

    def buscar_autor(self, kword):
        resultado = self.filter(
            Q(first_name__icontains=kword) | Q(last_name__icontains=kword)
        )
        return resultado