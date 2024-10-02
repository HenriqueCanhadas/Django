import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_oNJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    #Contact.objects.all().delete()
    #Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()
    
    django_contacts = []

    for _ in range(NUMBER_OF_oNJECTS):
        profile = fake.profile()
        email = profile['mail']
        primeiro_nome, ultimo_nome = profile['name'].split(' ', 1)
        celular = fake.phone_number()
        created_date:datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                primeiro_nome = primeiro_nome,
                ultimo_nome = ultimo_nome,
                celular = celular,
                created_date = created_date,
                description = description,
                category = category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)