from django.db import models

from agileLibrary.main.models import Laptop, Paper, Book, StudySpace


class Profile(models.Model):

    ID_NUMBER_MAX_LENGTH = 6
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    id_number = models.CharField(
        max_length=ID_NUMBER_MAX_LENGTH,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    loaned_books = models.ManyToManyField(
        Book,
        blank=True,
    )
    loaned_papers = models.ManyToManyField(
        Paper,
        blank=True,
    )

    loaned_laptop = models.OneToOneField(
        Laptop,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    booked_room = models.OneToOneField(
        StudySpace,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )




