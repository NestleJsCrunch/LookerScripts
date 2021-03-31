## Colab section ##
# install the sdk
!pip install looker-sdk
# set environ variables
import os
os.environ['LOOKERSDK_BASE_URL'] = '<insert api URL>'
os.environ['LOOKERSDK_API_VERSION'] = '3.1'
os.environ['LOOKERSDK_CLIENT_ID'] = '<insert api id>'
os.environ['LOOKERSDK_CLIENT_SECRET'] = '<insert api secret>'


# will need these for downloading the file from colab
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from google.colab import files
from oauth2client.client import GoogleCredentials
# auth stuff for download
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
## end Colab ##

## the actual script ##

# import and init
import looker_sdk
sdk = looker_sdk.init31("looker.ini")

import pandas as pd
import csv

# initialize variables
looks = [<insert comma delimited list of Look 'ID's>]
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
  
# colab specific - download the file
  from google.colab import files 
  files.download('output.xlsx')
