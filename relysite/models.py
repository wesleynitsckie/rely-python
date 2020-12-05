from django.db import models

class Sanction(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    income = models.FloatField()


class PEP(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()