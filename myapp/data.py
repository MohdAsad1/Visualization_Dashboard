
import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from myapp.models import UserProfile


def import_data():
    with open('/jsondata.json', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            my_data = UserProfile(
                end_year=item['end_year'],
                intensity=item['intensity'],
                sector=item['sector'],
                topic=item['topic'],
                insight=item['insight'],
                url=item['url'],
                region=item['region'],
                start_year=item['start_year'],
                impact=item['impact'],
                added=item['added'],
                published=item['published'],
                country=item['country'],
                relevance=item['relevance'],
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'],
                likelihood=item['likelihood'],
            )
            my_data.save()


import_data()
