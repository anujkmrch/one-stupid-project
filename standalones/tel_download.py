import getpass
import telnetlib
from datetime import datetime, timezone

import zipfile
import os
HOST = "somehost"

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
try:
    number_of_files = int(input("How many files you want to create"))
except Exception as e:
    print(e.msg())
    print('Quitting...')
    exit()

user, password = 'myname','mypassword'

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

dir_name = f"myuser_{timezone.now()}"
tn.write(f"mkdir {dir_name}\n")
tn.write("cd {dir_name}\n")
for i in range(1, number_of_files+1):
    tn.write(f"touch {i}.txt\n")

tn.write(f"zip {dir_name.zip} dirname\n")

tn.write("scp {user}@{HOST}:{dir_name}.zip {CUR_DIR}")

tn.read_until("password:\n")
tn.write(password+"\n")
tn.write("exit\n")

zip_file = os.path.join(CUR_DIR, dir_name)
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(CUR_DIR)

print (tn.read_all())