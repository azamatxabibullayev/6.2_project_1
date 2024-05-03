from django.db import models


# Create your models here.

class Cars(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return self.model


class ElectroCars(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'ElectroCars'

    def __str__(self):
        return self.model
