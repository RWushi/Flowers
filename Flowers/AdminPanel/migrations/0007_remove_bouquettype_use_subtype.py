# Generated by Django 5.0.6 on 2024-05-23 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0006_bouquettype_use_subtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bouquettype',
            name='use_subtype',
        ),
    ]
