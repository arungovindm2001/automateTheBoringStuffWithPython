import ezsheets

print('Opening Spreadsheet...')

ss = ezsheets.Spreadsheet('exampleForm')

print('Spreadsheet Opened')

sheet = ss[0]

print('Reading Spreadsheet...')

if 'Email' in sheet.getRow(1):
    emailindex = sheet.getRow(1).index('Email')
    emails = sheet.getColumn(emailindex+1)
    emails.pop(0)
    for email in emails:
        if email:
            print(email)
        else:
            break
else:
    print('Email not found in the spreadsheet')
