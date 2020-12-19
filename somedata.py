import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_project.settings')

from faker import Faker


import django
django.setup()

import random

from routs.models import Town , Hotels


data_fake= Faker()

towns=[ 'haifa','Eilat']

def add_town():
    s=Town.objects.get_or_create(name=random.choice(towns))[0]
    s.save()
    return s

def populate(N=10):
    for entry in range(N):
        towns= add_town()

        fake_name= data_fake.name()

        hotels= Hotels.objects.get_or_create(town=towns,name=fake_name)


if __name__=='__main__':
    print("population data.. please wait...")
    populate(20)
    print("populating completed")

