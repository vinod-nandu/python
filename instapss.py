# defining functions
import datetime
import pytz
import re
import base64
import paramiko
import os

from configparser import ConfigParser


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


def decrypt_config(config_sections):
    decry_dict = None
    hname = decrypt(config_file.get(config_sections, 'hostname'))
    uname = decrypt(config_file.get(config_sections, 'username'))
    pwd = decrypt(config_file.get(config_sections, 'password'))
    decry_dict = {"hostname": hname, "username": uname, "password": pwd}
    return decry_dict


def fn_ssh_execute(ssh_command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(decrypted_dict.get("hostname"), 22, decrypted_dict.get("username"), decrypted_dict.get("password"))
        stdin, stdout, stderr = ssh.exec_command(ssh_command)

        # Print the output
        for line in stdout.readlines():
            print(line.strip())
    finally:
        ssh.close()


# printing the starting line
print("WELCOME TO LEC INSTANT SUPPORT")

# Load config and encrypt it
config_file = ConfigParser()
print(config_file.read('config.ini'))
# print("Sections : ", config_file.sections())
decrypted_dict = decrypt_config("HKLPASS2B009")
_hostname = decrypted_dict.get("hostname")
_username = decrypted_dict.get("username")
_password = decrypted_dict.get("password")

# creating options
while True:
    print("\nMAIN MENU")
    print("1. S2BL Requests")
    print("2. eCas Requests")
    print("3. SCROE Requests")
    print("4. Support or Contact")
    print("5. Exit")
    choice1 = int(input("Enter the Choice:"))

    if choice1 == 1:
        print("\n S2BL Requests for the Production")
        print("1. List all Country Sameday files")  # sameday_all.sh
        print("2. List all CSL Sameday files")  # CSL_all.sh
        print("3. List all Country GLEL PSGL files")  # GLEL.sh
        print("4. Check for Licence Allocation Dir checks")
        print("5. Check for BT Rejection on any Country")  # rej.sh
        print("6. Exit")
        choice2 = int(input("Enter the Choice:"))

        if choice2 == 1:
            ssh_cmd = 'sh sameday_all.sh'
            fn_ssh_execute(ssh_cmd)
            break

        elif choice2 == 2:
            ssh_cmd = 'sh CSL_all.sh'
            fn_ssh_execute(ssh_cmd)
            break

        elif choice2 == 3:
            ssh_cmd = 'sh GLEL.sh'
            fn_ssh_execute(ssh_cmd)
            break

        elif choice2 == 4:
            mcode = input("Enter mcode to check dir allocations :")
            ssh_cmd = "find /itsapp/bg/data/" + str(mcode) + "/ -type d -print"
            print(ssh_cmd)
            fn_ssh_execute(ssh_cmd)
            break

        elif choice2 == 5:
            country = input("Enter Two letter Country code to check Rejection :")
            ssh_cmd = "sh rej.sh " + str(country) + " -2"
            print(ssh_cmd)
            fn_ssh_execute('sh rej.sh  VN -2')
            break

        else:
            print("Oops! Incorrect Choice.")

    elif choice1 == 2:
        print("\n eCas Requests for the Production")
        print("1. List all Country Sameday files")

    elif choice1 == 3:
        print("\n SCROE Requests for the Production")
        print("1. Download CTDS GTDS file for the day")
        print("2. Fetch PAIN file for a Payment Ref")

    elif choice1 == 4:
        print("For Support Write mail to ProductionEngineering-SCROE@sc.com")

    elif choice1 == 5:
        break
    else:
        print("Oops! Incorrect Choice.")
