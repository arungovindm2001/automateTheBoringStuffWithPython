import os, sys, PyPDF2, send2trash
from pathlib import Path

if len(sys.argv) < 2:
    print('py PDFParanoia.py [password]')
    sys.exit()
    
password = sys.argv[1]

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.pdf'):
            print('File found:'+filename)
            pdfFile = open(folderName+'/'+filename,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
                
            pdfWriter.encrypt(password)
            withoutDotPdf=filename.rstrip('.pdf')
            resultPdf = open(withoutDotPdf+'_encrypted.pdf', 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()

            decryptPdf = open(withoutDotPdf+'_encrypted.pdf', 'rb')
            decryptReader = PyPDF2.PdfFileReader(decryptPdf)

            if decryptReader.isEncrypted:
                print('File encrypted')
                print('Trying to decrypt...')
                decryptReader.decrypt(password)
                if decryptReader.decrypt(password) == 1:
                    print('File decrypted')
                    decryptPdf.close()
                    send2trash.send2trash(filename)
                    print('Original file sent to trash')
                else:
                    print('Could not decrypt file')
                    continue
            else:
                print('Error in encrypting',filename)
