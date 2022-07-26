import os
import shutil
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '_MJpD57MwlgAAAAAAAAAAQWPtnpiRAKdMZiLqVHAJqnz0F9yilMgv5Eb0b7t7LJ_'
    transferData = TransferData(access_token)

    file_from = input('Enter the File Path to Transfer:')
    file_to = input('Enter the File Path to upload to Dropbox:')

    transferData.upload_file(file_from, file_to)
    
    print("File has been moved")

if __name__ == '__main__':
    main()