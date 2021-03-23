/// credit: Eric Lyons
/// this script uses Looker's API to run a query 
/// and send those results to an sftp destination


import looker_sdk
import csv
import pysftp
#SET SFTP CREDENTIALS HERE. IT IS RECOMMENDED TO SET THEM IN ANOTHER FILE AND IMPORT THEM SECURELY
myHostname = "DOMAIN"
myUsername = "user"
myPassword = "PASSWORD"
####Initialize API/SDK for more info go here: https://pypi.org/project/looker-sdk/
#### IN THE SAME DIRECTORY CREATE AN INI FILE TO STORE API CREDENTIALS
## INITIALIZE THE API
from looker_sdk import methods31, models
sdk = looker_sdk.init31()  # or init40() for v4.0 API
me = sdk.me()
### GET THE LOOK BY PASSING THE LOOK ID
### WE ALSO WRITE THE FILE TO THE LOCAL DIRECTORY AS A CSV
look = sdk.run_look(look_id=12, result_format = "csv")
file = open('read.csv', 'w')
file.write(look)
file.close()
### HERE WE SEND THE CSV TO THE SFTP SERVER
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
print("Connection succesfully stablished ... ")
localFilePath = 'read.csv'
# Define the remote path where the file will be uploaded
remoteFilePath = '/files/NEWFILE/read.csv'
sftp.put(localFilePath, remoteFilePath)
