from _pydecimal import Decimal

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


class Buchung(models.Model):
    gast = models.ForeignKey(Gast, on_delete=models.CASCADE)
    datum_von = models.DateField(blank=True, null=True)
    datum_bis = models.DateField(blank=True, null=True)
    preis: Decimal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    kosten_chiara = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    anzahl_gaeste = models.IntegerField(default=2)
    kommentar = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "buchungen"

    def __str__(self):
        result = "{} - {}".format(self.datum_von, self.datum_bis)
        return result

