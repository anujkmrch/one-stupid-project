
import argparse
import sys
import os
import django
from faker import Faker
from faker.providers import internet


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--length', dest='length', action='store_const',
                    const=sum, default=10,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

length = args.length
from myapi.models import Device
fake = Faker()
devices = []
for i in range(0,length):
    sap_id = fake.pystr(max_chars=14)
    loopback =fake.ipv4_private()
    hostname = fake.hostname().split('.')[0]
    mac_address = fake.mac_address()

    devices.append(Device(sap_id=sap_id, hostname=hostname, loopback=loopback, mac_address=mac_address))

if devices:
    Device.objects.bulk_create(devices)





