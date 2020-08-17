from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

credentials_file_path = 'credentials/credentials.json'
credentials_file_path = 'dash/credentials.json'
clientsecret_file_path = 'dash/client_secret.json'

# SCOPES = 'https://www.googleapis.com/auth/drive'
# SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# define store
store = file.Storage(credentials_file_path)
# credentials = store.get()
credentials = None

if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(clientsecret_file_path, SCOPES)
    credentials = tools.run_flow(flow, store)

# define API service
http = credentials.authorize(Http())
drive = discovery.build('drive', 'v3', http=http)

# define a function


print(drive)





