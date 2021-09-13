from django.db import models

# Create your models here.


class VINData(models.Model):
    vincode = models.CharField(max_length=17, unique=True)
    year = models.PositiveBigIntegerField(null=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    state = models.CharField(max_length=10, null=True)
    doors = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.vincode

    class Meta:
        verbose_name = 'Vehicle ID'
        verbose_name_plural = 'Vehicle IDs'
