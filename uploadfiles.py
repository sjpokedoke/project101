import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    
    def files_upload(self, source, dest):
        dbx = dropbox.Dropbox(self.accesstoken)

        for root, dirs, files in os.walk(source):
            for filename in files:
                localpath = os.path.join(root, filename)
                relativepath = os.path.relpath(localpath, source)
                dropboxpath = os.path.join(root, filename)
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxpath, mode=WriteMode('overwrite'))
def main():
    accesstoken = 'SM_hNyzFWr0AAAAAAAAAAS-_WaaxXOtrqd7yyHIa94yTNU6LIfUaefLjpeK7X7PT'
    transferData = TransferData(accesstoken)

    source = input('Enter the folder path to transfer: ')
    dest = input('Enter the full path to upload to dropbox: ')

    transferData.uploadfiles(source, dest)
    print('File has been moved successfully')
main()