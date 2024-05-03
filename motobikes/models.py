from django.db import models


# Create your models here.


class Moto(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'Motobikes'

    def __str__(self):
        return self.model
