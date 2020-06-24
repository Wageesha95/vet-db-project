from django.db import models

# Create your models here.


class Division(models.Model):

    division_code = models.CharField(max_length=64)
    division_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.division_name} - ({self.division_code})"


class Farm(models.Model):
    farm_name = models.CharField(max_length=64)
    division = models.ForeignKey(Division,
                                 on_delete=models.CASCADE,
                                 related_name="farms")

    def __str__(self):
        return f"{self.farm_name} - {self.division}"
