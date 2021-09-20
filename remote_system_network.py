import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("Connecting........")

ssh_client.connect(hostname="127.0.0.1", port=22,username="superuser", password="root")

stdin, stdout, stderr = ssh_client.exec_command("cat /proc/loadavg\n")
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client.exec_command("uptime -s\n")
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client.exec_command("free -m\n")
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client.exec_command("route -n\n")
print(stdout.read().decode())

time.sleep(1)

if ssh_client.get_transport().is_active() == True:
    print("Disconnecting.............")
    ssh_client.close()
