# Generated by Django 5.0.6 on 2024-05-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0005_alter_flowersubtype_options_flowercolor_flower_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquettype',
            name='use_subtype',
            field=models.BooleanField(default=True, verbose_name='Использовать подвид'),
        ),
    ]
