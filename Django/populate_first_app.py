import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Django.settings')

import django
django.setup()

##Fake Pop Scrpit
import random
from fitst_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketpalce','news','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        
        #get the topic for the entry
        top = add_topic()


        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create the fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete")
