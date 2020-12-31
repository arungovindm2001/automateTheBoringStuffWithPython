import os, shutil
from pathlib import Path
p=Path.home()
for folderName, subfolders, filenames in os.walk(p/'cse'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        if filename.endswith('.pdf') or filename.endswith('.jpg'):
            shutil.copy(p/'cse'/folderName/filename, p/'copyfolder'/filename)
            print('Ok')
    print('')
