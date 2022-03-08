from django.db import models


class Cargos(models.Model):
    capacity = models.IntegerField(
        default=100,
    )

# on-hold stacks
# laptops shelters
