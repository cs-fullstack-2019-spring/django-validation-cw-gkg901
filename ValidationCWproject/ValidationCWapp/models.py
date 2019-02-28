from django.db import models


# Create your models here.
class CarModel(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(default=2019, null=False)
    mpg = models.DecimalField(max_digits=999, decimal_places=2)

    def __str__(self):
        return self.make



