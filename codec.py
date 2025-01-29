import base64
from configparser import ConfigParser
import paramiko


def encrypt(plain_text):
    plain_text_bytes = plain_text.encode("ascii")

    base64_bytes = base64.b64encode(plain_text_bytes)
    base64_string = base64_bytes.decode("ascii")
    return f"{base64_string}"


def decrypt(encrypted_text):
    base64_bytes = encrypted_text.encode("ascii")

    decrypted_string_bytes = base64.b64decode(base64_bytes)
    decrypted_string = decrypted_string_bytes.decode("ascii")

    return f"{decrypted_string}"


def decrypt_config(configur_sections):
    decry_dict = None
    hname = decrypt(configur.get(configur_sections, 'hostname'))
    uname = decrypt(configur.get(configur_sections, 'username'))
    pwd = decrypt(configur.get(configur_sections, 'password'))
    decry_dict = {"hostname": hname, "username": uname, "password": pwd }
    return decry_dict




# print(encrypt("Tower14#FiveD"))

# print(decrypt("Vmlub2Q="))

# input("input any key to close")
# f = open("App.config", "r")
# print(f.read())


configur = ConfigParser()
print(configur.read('config.ini'))

print("Sections : ", configur.sections())

decrypted_dict = decrypt_config("HKLPASS2B009")
#print(decrypted_dict)
print(decrypted_dict.get("hostname"))
print(encrypt("10.7.176.18"))
# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(decrypted_dict.get("hostname"), 22, decrypted_dict.get("username"), decrypted_dict.get("password"))
    stdin, stdout, stderr = ssh.exec_command('ls -ltr *.txt')

    # Print the output
    for line in stdout.readlines():
        print(line.strip())
finally:
    ssh.close()
