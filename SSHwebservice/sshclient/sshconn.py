import paramiko
import time


def connect():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="localhost", port=10000, username="admin", password="admin")
    stdin,stdout,stderr = ssh_client.exec_command("show running-conf")
    return stdout.read().decode()
