# Generated by Django 3.1.3 on 2020-12-09 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201209_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bestellung',
            options={'verbose_name_plural': 'Bestellungen'},
        ),
        migrations.AlterModelOptions(
            name='kunde',
            options={'verbose_name_plural': 'Kunden'},
        ),
    ]
