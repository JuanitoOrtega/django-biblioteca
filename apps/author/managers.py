from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):
    """ managers para el modelo author """

    def buscar_autor(self, kword):
        resultado = self.filter(first_name__icontains=kword)
        return resultado

    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(first_name__icontains=kword) | Q(last_name__icontains=kword) # Operador ó
        )
        return resultado

    def buscar_autor3(self, kword):
        # resultado = self.filter(first_name__icontains=kword).exclude(nationality='AR')
        resultado = self.filter(first_name__icontains=kword).exclude(Q(nationality__icontains='AR') | Q(nationality='PE'))
        return resultado

    def buscar_autor4(self, kword):
        resultado = self.filter(age__gt=50, age__lt=75).order_by('-first_name', 'first_name') # gt mayor que, lt menor que, la coma es operador y
        return resultado