from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discont', 'Discont')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptons', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptons', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptons', on_delete=models.PROTECT)