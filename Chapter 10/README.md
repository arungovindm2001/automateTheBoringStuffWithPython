## 1. What is the difference between shutil.copy() and shutil.copytree() ?

`shutil.copy()` - copies a single file<br />
`shutil.copytree()` - copies an entire folder and every folder and file contained in it.

## 2. What function is used to rename files?

`shutil.move(originalpath,newpathwithdifferentfilename)`

## 3. What is the difference between the delete functions in the send2trash and shutil modules?

send2trash will delete the file and send to the Recycle Bin.<br />
shutil will delete the file permanently.

## 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

`zipfile.ZipFile('example.zip')`

