import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def popgen(N=5):
    for i in range(N):
        ffirst = fakegen.first_name()
        flastname = fakegen.last_name()
        femail = fakegen.email()
        webpage = User.objects.get_or_create(firstname = ffirst, lastname = flastname, email= femail)

if __name__ == '__main__':
    print ("populating script !")
    popgen(21)
    print ("Poplutaing complete!")
