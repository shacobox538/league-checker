from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    uco = models.CharField(max_length=6, default="")
    name = models.CharField(max_length=20, default="")
    surname = models.CharField(max_length=20, default="")
    ROLES = (
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin'),
    )
    role = models.CharField(max_length=1, choices=ROLES)


class Summoner(models.Model):
    name = models.CharField(max_length=16)
    league = models.JSONField(default=dict)
    summoner = models.JSONField(default=dict)
    mastery = models.JSONField(default=list)
    matches = models.JSONField(default=list)

