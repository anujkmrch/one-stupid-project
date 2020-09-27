import os
import subprocess

msg = subprocess.check_output("cat /proc/loadavg | awk '{print $1}'", shell=True)
current_load = int(msg.decode("utf-8").strip().strip('.')[0])
threshold = 20
if current_load >= threshold:
    subprocess.check_output("systemctl restart apache2", shell=True)