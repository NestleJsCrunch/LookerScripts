# get looker sdk
!pip install looker-sdk
import looker_sdk

# I'm using colab and setting these as environment variables. you would normally place these in the sdk config file
import os
os.environ['LOOKERSDK_BASE_URL'] = '<insert api url>'
os.environ['LOOKERSDK_API_VERSION'] = '3.1'
os.environ['LOOKERSDK_CLIENT_ID'] = '<client id>'
os.environ['LOOKERSDK_CLIENT_SECRET'] = '<client secret>'

# init the sdk
sdk = looker_sdk.init31("looker.ini")

import pandas as pd
import csv

# colab specific 
from google.colab import files

!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from google.colab import files
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

### the actual loop ###

looks = [<comma delimited list of Look 'IDs', eg: '1','2','3']
lislen = len(looks)

with pd.ExcelWriter('output.xlsx') as writer: 
  for i in range(lislen):
    data = sdk.run_look(looks[i],'csv')
    with open('big.csv', 'w', newline='') as file:
        file.write(data)
    df = pd.read_table('big.csv', delimiter =",",engine='python')
    df.to_excel(writer, sheet_name=('Tab '+ str(i)))
  
# colab specific
  files.download('output.xlsx')
