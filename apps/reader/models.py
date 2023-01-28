from django.utils import timezone
from django.db import models
from django_countries.fields import CountryField

from apps.book.models import Book
from .managers import LendManager


class Reader(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Nombres')
    last_name = models.CharField(max_length=100, verbose_name='Apellidos')
    nationality = CountryField(blank_label='Seleccionar país', verbose_name='Nacionalidad')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')
    age = models.IntegerField(blank=True, null=True, verbose_name='Edad')

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def get_age(self):
        if self.birth_date is not None:
            today = timezone.now().date()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return f'{age} años'
        else:
            return None

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self.birth_date:
            today = timezone.now().date()
            self.age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lend(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Lector')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_lend', verbose_name='Libro')
    lend_date = models.DateTimeField(auto_now_add=False, verbose_name='Fecha de préstamo')
    return_date = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='Fecha de devolución')
    returned = models.BooleanField(default=False, verbose_name='Devuelto')

    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'

    objects = LendManager()

    def __str__(self):
        return f'{self.book.title}'