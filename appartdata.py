import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project.settings')

from faker import Faker


import django
django.setup()

import random

from routs.models import Appartement


data_fake= Faker()

app=Appartement.objects.get(id=2)

def add_app():
    s=Appartement.objects.get_or_create(town=random.choice(app))[0]
    s.save()
    return s

def populate(N=10):
    for entry in range(N):
        app= add_app()

        fake_adress= data_fake.adress()

        appart= Appartement.objects.get_or_create(town=app,name__adress=fake_adress)


if __name__=='__main__':
    print("population data.. please wait...")
    populate(20)
    print("populating completed")

