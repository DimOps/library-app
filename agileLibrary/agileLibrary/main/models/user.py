from django.db import models


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