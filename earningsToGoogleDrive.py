import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import date


pd.option_context('display.max_rows', None, 'display.max_columns', None)
earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings')[0]
earnings.to_csv(r'earnings_{}.csv'.format(date.today()), index=None)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


# View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  # Get the folder ID that you want
  if(file['title'] == "Earnings"):
      fileID = file['id']

file1 = drive.CreateFile({"mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
file1.SetContentFile("earnings_{}.csv".format(date.today()))
file1.Upload() # Upload the file.
print ('\n')
print('Created file %s with mimeType %s with id %s' % (file1['title'], file1['mimeType'], file1['id']))


emails = [
    'pradhamesh007@gmail.com',
    'akkiraju.pradhamesh@gmail.com'
]

for email in emails:
    new_permission = {
        'value': email,
        'type': 'user',
        'role': 'reader'
    }
    test = file1.InsertPermission(new_permission)
    print ("The file has been shared to ", email)