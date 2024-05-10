import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
import django
django.setup()
from testapps.models import HydJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num +=str(randint(0,9))
    return int(num)
def pop(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('PM',"SE","TL",'SD','AE'))
        feligibility=fake.random_element(elements=('BTECH',"MSC",'MCA','CS','PHD'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber = phonenumbergen()
        Hyd_records=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber = fphonenumber)
n=int(input('enter ur recordes:'))
pop(n)
print(f'{n} no of records inserted....')