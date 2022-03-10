from django.db import models


class StudySpace(models.Model):

    room_number = models.CharField(
        max_length=5,
    )

    sector = models.CharField(
        max_length=10,
    )

    level = models.IntegerField(
        default=1,
    )

    capacity = models.IntegerField(
        default=4,
    )

    smartBoard = models.BooleanField(
        default=False,
    )

    is_booked = models.BooleanField(
        default=False,
    )
