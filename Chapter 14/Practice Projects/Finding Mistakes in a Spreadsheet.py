import ezsheets

ss=ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet=ss[0]

print('Spreadsheet opened')

print('Reading Spreadsheet')

for rowNum in range(2,sheet.rowCount):
    if int(sheet.getRow(rowNum)[0]) * int(sheet.getRow(rowNum)[1]) != int(sheet.getRow(rowNum)[2]):
        print('Mistake found at Row',rowNum)
        break
