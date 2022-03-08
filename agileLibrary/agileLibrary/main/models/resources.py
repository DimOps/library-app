from django.db import models


class Book(models.Model):

    ISBN_MAX_LENGTH = 13
    TITLE_MAX_LENGTH = 300
    AUTHORS_MAX_LENGTH = 300
    PUBLISHER_MAX_LENGTH = 300

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    authors = models.CharField(
        max_length=AUTHORS_MAX_LENGTH,
    )

    isbn = models.CharField(
        max_length=ISBN_MAX_LENGTH,
    )

    publisher = models.CharField(
        max_length=PUBLISHER_MAX_LENGTH,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )


class Paper(models.Model):
    TITLE_MAX_LENGTH = 300
    AUTHORS_MAX_LENGTH = 300

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    authors = models.CharField(
        max_length=300,
    )

    doi = models.URLField(
        blank=True,
        null=True,
    )

    published = models.SmallIntegerField()

    description = models.TextField(
        blank=True,
        null=True,
    )


class Laptop(models.Model):
    ID_MAX_LENGTH = 10
    MANUFACTURER_MAX_LENGTH = 30
    MODEL_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 20

    laptop_id = models.CharField(
        max_length=ID_MAX_LENGTH,
    )

    manufacturer = models.CharField(
        max_length=MANUFACTURER_MAX_LENGTH,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
    )