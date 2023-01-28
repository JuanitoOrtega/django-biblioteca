import datetime
from django.db import models
from django.db.models import Avg, Sum


class LendManager(models.Manager):
    """ managers para el modelo lend """

    def books_average_age(self):
        result = self.filter(book__id='13').aggregate(average_age=Avg('reader__age'), sum_age=Sum('reader__age'))
        return result