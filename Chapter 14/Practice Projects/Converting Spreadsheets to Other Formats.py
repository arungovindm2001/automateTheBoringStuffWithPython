import ezsheets
import time

print('Copy the spreadsheet file to this script\'s directory')
time.sleep(1)

print('Enter the extension of file')
extension=input()

print('Enter the name of the file (with extension)')
file=input()

print('Uploading file...')
ss=ezsheets.upload(file)
print('File uploaded')

filename=file.rstrip(extension)

ss=ezsheets.Spreadsheet(filename)

ss.downloadAsExcel()
print('Downloaded as Excel')

ss.downloadAsODS()
print('Downloaded as ODS')

ss.downloadAsCSV()
print('Downloaded as CSV')

ss.downloadAsTSV()
print('Downloaded as TSV')

ss.downloadAsPDF()
print('Downloaded as PDF')

ss.downloadAsHTML()
print('Downloaded as HTML')

ss.delete(permanent=True)
print('Deleted the spreadsheet from Google Drive successfully')



