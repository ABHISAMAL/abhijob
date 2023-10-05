import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','abhijobproject.settings')
import django
django.setup()

from testapp.models import HydJobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1 = randint(6, 9)
    num = '' + str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)
def papulate(n):
    for i in range(n):
        fdate = fake.date()
        fcomany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_job_record = HydJobs.objects.get_or_create(
            date=fdate,
            company=fcomany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n=int(input('Nomber of records :'))
papulate(n)
print(f'{n} records insert sucessfully...')




from testapp.models import PuneJobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1 = randint(6, 9)
    num = '' + str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)
def papulate(n):
    for i in range(n):
        fdate = fake.date()
        fcomany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_job_record = HydJobs.objects.get_or_create(
            date=fdate,
            company=fcomany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n=int(input('Nomber of records :'))
papulate(n)
print(f'{n} records insert sucessfully...')
