## 1. What three files do you need for EZSheets to access Google Sheets?

To access Google Sheets, you need a credentials file named credentials.json, a token file for google sheets named token-sheets.pickle and a token file for Google Drive named token-drive.pickle.

## 2. What two types of objects does EZSheets have?

`ezsheets.Spreadsheet`
`ezheets.Sheet`

## 3. How can you create an Excel file from a Google Sheet spreadsheet?

We can download the Google Sheet as an Excel file. To do this we call `downloadAsExcel()` ethod.

## 4. How can you create a Google Sheet spreadsheet from an Excel file?

We can upload an Excel file to the Google Drive and create a Google Sheet spreadsheet. To do this, we call the ezsheets.upload() method with filename as its argument.

## 5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?

`ss["Students"]["B2"]`

## 6. How can you find the column letters for column 999?

`ezsheets.getColumnLetterOf(999)`

## 7. How can you find out how many rows and columns a sheet has?

rowCount and columnCount will give the number of rows and columns respectively.

## 8. How do you delete a spreadsheet? Is this deletion permanent?

We call the `delete()` method to delete a spreadsheet. This deletion will send the spreadsheet to Google Drive Trash.<br />
If you want to delete the spreadsheet permanently, we add permanent keyword argument as `True` to `delete()` method.<br />
For example: `delete(permanent=True)`

## 9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?

`createSpreadsheet()` - Creates a Spreadsheet
`createSheet()` - Creates a new Sheet

## 10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?

According to Google’s developer guidelines, users are restricted to creating 250 new spreadsheets a day, and free Google accounts can perform 100 read and 100 write requests per 100 seconds. Attempting to exceed this quota will raise the googleapiclient.errors.HttpError “Quota exceeded for quota group” exception.

