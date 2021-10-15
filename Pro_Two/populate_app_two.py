import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Pro_Two.settings')

import django
django.setup()

##FAKE POPULATION SCRIPT
import random
from App_Two.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_eamil = fakegen.email()

        #New Entry 
        user = User.objects.get_or_create(First_Name=fake_first_name,
        Last_Name=fake_last_name,
        Email=fake_eamil
        )[0]

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(500)
    print("COMPLETE")

