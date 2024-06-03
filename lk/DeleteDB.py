import paramiko
import time

infobaseUser = input(str("Enter Infobase User: " )) 
infobasePwd = input(str("Enter Infobase Password: " )) 
infobaseId = input(str("Enter Infobase ID: " )) 
infobase_name = input(str("Enter Infobase Name: " )) 

def DeleteDB(infobaseUser, infobasePwd,infobaseId,infobase_name):
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.100.48.93', username='root', password='', look_for_keys=True, key_filename='/opt/1cv8/x86_64/8.3.23.2040/rac infobase --cluster=f927fdde-74f4-4394-9a8f-43484ca7bd84 summary list')

    #delete database
    stdin, stdout, stderr = client.exec_command(f'/opt/1cv8/x86_64/8.3.23.2040/rac infobase --cluster=f927fdde-74f4-4394-9a8f-43484ca7bd84 drop --infobase-user={infobaseUser} --infobase-pwd={infobasePwd} --infobase={infobaseId}')
    for line in stdout:
            print(line.strip('\n'))
    time.sleep(1) 

    #Delete Publication
    stdin, stdout, stderr = client.exec_command(f'/opt/1cv8/x86_64/8.3.23.2040/webinst -delete -apache24 -wsdir {infobase_name} -dir /var/www/{infobase_name}/ -connstr "Srvr=localhost;Ref={infobase_name};" -confPath /etc/apache2/apache2.conf')
    for line in stdout:
           print(line.strip('\n'))
    time.sleep(1)

    #Reload apache2
    stdin, stdout, stderr = client.exec_command('systemctl reload apache2')
    for line in stdout:
            print(line.strip('\n'))
    time.sleep(1)

if __name__ == '__main__':
        DeleteDB(infobaseUser=infobaseUser , infobasePwd=infobasePwd, infobaseId=infobaseId, infobase_name=infobase_name)







