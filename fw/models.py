from django.db import models
from django.conf import settings
from django.utils import timezone


class Gast(models.Model):
    ANREDE = (
        ('Herr', 'Herr'),
        ('Frau', 'Frau'),
        ('Familie', 'Familie'),
        ('Mr.', 'Mister'),
        ('Mrs.', 'Miss'),
    )
    nachname = models.CharField(max_length=255)
    vorname = models.CharField(max_length=255, blank=True, null=True)
    anrede = models.CharField(max_length=20, blank=True, null=True, choices=ANREDE)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        result = "{} {} {}".format(self.anrede, self.vorname, self.nachname)
        return result

    class Meta:
        verbose_name_plural = "gäste"

    def full_name(self):
        fname = "{} {} {}".format(self.anrede, self.vorname, self.nachname)
        return fname
