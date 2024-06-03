import paramiko
import time

infobase_name = input(str("Enter Infobase Name: " )) 
descr = input(str("Enter Infobase description: " ))

def CreateAndPublishDB(infobase_name, descr):
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.100.48.93', username='root', password='', look_for_keys=True, key_filename='/opt/1cv8/x86_64/8.3.23.2040/rac infobase --cluster=f927fdde-74f4-4394-9a8f-43484ca7bd84 summary list')

    #Create database
    stdin, stdout, stderr = client.exec_command(f'/opt/1cv8/x86_64/8.3.23.2040/rac infobase --cluster=f927fdde-74f4-4394-9a8f-43484ca7bd84 create --create-database --name={infobase_name} --descr={descr} --dbms=PostgreSQL --db-server=localhost --db-name={infobase_name} --locale=ru --db-user=postgres --db-pwd=Qwer-123 --license-distribution=allow')
    for line in stdout:
            print(line.strip('\n'))
    time.sleep(1) 

    #Publish database
    stdin, stdout, stderr = client.exec_command(f'/opt/1cv8/x86_64/8.3.23.2040/webinst -publish -apache24 -wsdir {infobase_name} -dir /var/www/{infobase_name}/ -connstr "Srvr=localhost;Ref={infobase_name};" -confPath /etc/apache2/apache2.conf')
    for line in stdout:
            print(line.strip('\n'))
    time.sleep(1)

    #Reload apache2
    stdin, stdout, stderr = client.exec_command('systemctl reload apache2')
    for line in stdout:
            print(line.strip('\n'))
    time.sleep(1)


if __name__ == '__main__':
        CreateAndPublishDB(infobase_name=infobase_name , descr=descr)
