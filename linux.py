import paramiko

# Define the server details
hostname = '10.XXXXXXXX'
port = 22
username = 'uid'
password = 'pwd'

# Create an SSH client
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connectto a Server
    ssh.connect(hostname, port, username, password)

    # Excecute a command

    stdin, stdout, stderr = ssh.exec_command('sh eve_rpt.sh')

    # Print the output
    for line in stdout.readlines():
        print(line.strip())

    transport = paramiko.Transport((hostname, port))
    transport.connect(None, username, password)


    # Go!
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Download
    # filepath = "/prd/Scroe/fileprocessor/trafigura/ctdsgtdsh2h/completed/*20241206*.xlsx"
    # localpath = "C:\\Users\uid\Downloads\"
    # sftp.get(filepath,localpath)

    #sftp.get('/prd/xxxx/fileprocessor/xxxxxxxxxxx/ctdsgtdsh2h/completed/xxxxxxx.xlsx',
             #'C:\\Users\\uid\\rrrrrrrrrrr\\ssssssssss.xlsx')


    # Upload
    filepath = "/home/uid/Hello1.txt"
    localpath = "C:\\Users\\uid\\Downloads\\Hello1.txt"
    sftp.put(localpath,filepath)
    sftp.chmod(filepath, 0o777)

finally:
    ssh.close()
