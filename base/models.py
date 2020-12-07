from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Sanction(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    income = models.FloatField()

    def __str__(self):
        return self.first_name

class PEP(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()

    def __str__(self):
        return self.first_name

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    transaction_blob = models.JSONField()
    is_person_on_sanction_list = models.BooleanField(default=False)
    is_person_on_pep_list = models.BooleanField(default=False)
    confirm_on_sanction_list = models.BooleanField(default=False)
    confirm_on_pep_list = models.BooleanField(default=False)

    class Status(models.TextChoices):
        INIT = 'INIT', _('Initialized')
        SANCTIONCHECK = 'SC', _('Sanction Check')
        SANCTIONCHECKCOMPLETED = 'SCC', _('Sanction Check Completed')
        PEPCHECK = 'PC', _('PEP Check')
        PEPCHECKCOMPLETED = 'PCC', _('PEP Check Completed')
        ASSESSMENT = 'AS', _('Assessment')
        ACCEPTED = 'ACCEPTED', _('Accepted')
        DENIED = 'DENIED', _('Denied')

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SANCTIONCHECK,
    )

    