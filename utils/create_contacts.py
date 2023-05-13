import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000 # informe o numero de contatos que seram inseridos na base de dados

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact
    from django.contrib.auth.models import User

    # Para apaga a base de dados antiga descomente as linhas abaixo.
    
    #Contact.objects.all().delete()
    #Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    user = User.objects.get(username="") # insira o nome de usuario e descomente a o owner na linha 61
    categories = ['Amigos', 'Família', 'Conhecidos'] # adcione suas categorias aqui

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)
        

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
                # descomente essa linha se quiser que os contatos sejam visiveis fora da area administrativa
                #owner=user
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
