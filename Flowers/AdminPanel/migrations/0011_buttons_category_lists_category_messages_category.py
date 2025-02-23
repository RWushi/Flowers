# Generated by Django 5.0.6 on 2024-05-23 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0010_rename_category_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttons',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.categories'),
        ),
        migrations.AddField(
            model_name='lists',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.categories'),
        ),
        migrations.AddField(
            model_name='messages',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.categories'),
        ),
    ]
