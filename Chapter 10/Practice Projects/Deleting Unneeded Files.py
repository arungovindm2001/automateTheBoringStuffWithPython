import os, shutil,send2trash
from pathlib import Path
p=Path.home()
for folderName, subfolders, filenames in os.walk(p/'cse'):
    print('The current folder is ' + folderName)
    if os.path.getsize(p/'cse'/folderName) > 104857600:
            os.rmtree(p/'cse'/folderName)
            print('File deleted')
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        if os.path.getsize(p/'cse'/folderName) > 104857600:
            os.rmtree(p/'cse'/folderName)
            print('File deleted')
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        if os.path.getsize(p/'cse'/folderName/filename) > 104857600:
            send2trash.send2trash(p/'cse'/folderName/filename)
            print('File deleted')
    print('')
