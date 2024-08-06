import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Flowers.settings')
django.setup()

from django.db.models import Q
from AdminPanel.models import System, Buttons, Messages, Lists, ListTitles


def get_data_by_category(category_names):
    if isinstance(category_names, str):
        category_names = [category_names]

    models = [System, Buttons, Messages, Lists, ListTitles]

    results = {}

    for model in models:
        filtered_data = model.objects.filter(Q(category__name__in=category_names))
        for item in filtered_data:
            variable = getattr(item, 'variable', None)
            text = getattr(item, 'text', None)
            if variable and text:
                results[variable] = text

    response = json.dumps(results, ensure_ascii=False)
    return response