import paramiko
import time

""" infobaseID = ''
infobaseName = ''
infobaseDescription = '' """

def chdbn():
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.100.48.93', username='root', password='', look_for_keys=True, key_filename='/Users/almaz/Documents/GitHub/paramiko_fastapi/1c_create_db/lk/id_rsa.pub')

    #Check existing bases
    stdin, stdout, stderr = client.exec_command('/opt/1cv8/x86_64/8.3.23.2040/rac infobase --cluster=f927fdde-74f4-4394-9a8f-43484ca7bd84 summary list')
    
    outputDB = stdout.read().decode('utf-8')

    #infobase ID
    global infobaseIDData
    infobaseID = outputDB.splitlines()[0]
    
    infobaseIDAll = infobaseID.split(": ")
    
    if len(infobaseIDAll) > 1:
        infobaseIDData = infobaseIDAll[1]
    else:
        infobaseIDData = None

    print(infobaseIDData)

    #print(infobaseID)

    #infobase Name
    global infobaseNameData
    infobaseName = outputDB.splitlines()[1]
    
    infobaseNameAll = infobaseName.split(": ")
    
    if len(infobaseNameAll) > 1:
        infobaseNameData = infobaseNameAll[1]
    else:
        infobaseNameData = None

    print(infobaseNameData)

    #infobase Description
    global infobaseDescriptionData

    infobaseDescription = outputDB.splitlines()[2]

    infobaseDescriptionAll = infobaseDescription.split(": ")
    
    if len(infobaseDescriptionAll) > 1:
        infobaseDescriptionData = infobaseDescriptionAll[1]
    else:
        infobaseDescriptionData = None

    print(infobaseDescriptionData)

    #print(infobaseDescription)


    client.close()


if __name__ == '__main__':
        chdbn()




