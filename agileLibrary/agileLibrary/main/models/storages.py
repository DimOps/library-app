from django.db import models

from agileLibrary.main.models import Laptop


class Trolley(models.Model):
    capacity = models.IntegerField(
        default=100,
    )


class LaptopDrawer(models.Model):
    id_number = models.CharField(
        max_length=5,
    )

    laptop = models.OneToOneField(
        Laptop,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class ReservedBooksShelf(models.Model):

    alphabetic_block = models.CharField(
        max_length=1,
    )

