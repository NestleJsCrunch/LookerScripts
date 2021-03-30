# get looker sdk
!pip install looker-sdk
import looker_sdk

import os
os.environ['LOOKERSDK_BASE_URL'] = 'https://dcl.api.dev.looker.com'
os.environ['LOOKERSDK_API_VERSION'] = '3.1'
os.environ['LOOKERSDK_CLIENT_ID'] = 'BPdgzrT9nqrJHjwbJByn'
os.environ['LOOKERSDK_CLIENT_SECRET'] = 'Kyg2D2xdd95B4RpYc3RRBgPN'

# init the sdk
sdk = looker_sdk.init31("looker.ini")

import pandas as pd
import csv

# doing this in colab
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

### the actual loop

# initialize variables
looks = ['2131', '2132', '2133']
lislen = len(looks)
titles = []

# loop to get look titles for tabs
for i in range(lislen):
  data = sdk.look(looks[i])
  title = data.title
  titles.append(title)

# loop to create the tabbed output file
with pd.ExcelWriter('output.xlsx') as writer: 
  for i in range(lislen):
    data = sdk.run_look(looks[i],'csv')
    with open('big.csv', 'w', newline='') as file:
        file.write(data)
    df = pd.read_table('big.csv', delimiter =",",engine='python')
    df.to_excel(writer, sheet_name=(titles[i]))
  
# colab specific
  files.download('output.xlsx')
