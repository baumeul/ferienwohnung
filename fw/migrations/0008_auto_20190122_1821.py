# Generated by Django 2.1.5 on 2019-01-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fw', '0007_auto_20190122_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buchung',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
