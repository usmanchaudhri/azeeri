from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import json
import pprint
import datetime
import pickle
import os.path

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """
    Shows basic usage of the Drive v3 API.
    :return:
    """

    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('dash/client_secret.json', SCOPES)
            creds = flow.run_local_server()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the drive v2 API
    # results = service.activities().list(source='drive.google.com',
    #                                     drive_ancestorId='root', pageSize=10).execute()
    # activities = results.get('activities', [])
    # if not activities:
    #     print('No activity.')
    # else:
    #     print('Recent activity:')
    #     for activity in activities:
    #         event = activity['combinedEvent']
    #         user = event.get('user', None)
    #         target = event.get('target', None)
    #         if user is None or target is None:
    #             continue
    #         time = datetime.datetime.fromtimestamp(int(event['eventTimeMillis'])/1000)
    #         print(u'{0}: {1}, {2}, {3}, ({4})'.format(time, user['name'],
    #                                                   event['primaryEventType'],
    #                                                   target['name'],
    #                                                   target['mimeType']))
    results = service.files().list(pageSize=200, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:', len(items))
        for item in items:
            # print(u'{0} ({0})'.format(item['name'], item['id'] ))
            print(u'{0}'.format(item))

    print('Item Types', type(items))
    result = json.dumps(items)
    print(result)

if __name__ == "__main__":
    main()








