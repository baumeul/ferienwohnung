# Generated by Django 2.1.5 on 2019-01-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nachname', models.CharField(max_length=255)),
                ('vorname', models.CharField(max_length=255)),
                ('anrede', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'gäste',
            },
        ),
    ]
