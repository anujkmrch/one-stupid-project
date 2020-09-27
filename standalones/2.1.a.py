import telnetlib

HOST = "localhost"
user,password = "myuser","mypassword"
some_path = '/'
tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until("Password: ")
    tn.write(password.encode('ascii') + b"\n")

# tn.write("df\n")
# tn.write("df -ih /\n")
# tn.write(f"ls {some_path}\n")
tn.write("exit\n")

print(tn.read_all().decode('ascii'))
