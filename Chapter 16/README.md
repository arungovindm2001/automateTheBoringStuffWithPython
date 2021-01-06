## 1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?

Excel spreadsheets can have more than one sheet, they can store values other than strings, cells can have varying fonts, sizes, widths and heights, one can embed images and charts too.

## 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

open() method is passed.<br />
For example:<br />
`csv.reader(open(<file-name-in-csv-format>))`<br />
`csv.writer(open(<file-name-in-csv-format>, 'w', newline=''))`


## 3. What modes do File objects for reader and writer objects need to be opened in?

reader object is opened in read mode ('r' in short)<br />
writer object is opened in write mode ('w' in short)

## 4. What method takes a list argument and writes it to a CSV file?

`writerow()`

## 5. What do the delimiter and lineterminator keyword arguments do?

The delimiter and lineterminator arguments are passed in `csv.writer()`<br />
The delimiter is the character that appears between cells on a row. Therefore the delimiter argument changes the string used to separate cells in a row. By default, the delimiter for a CSV file is a comma.<br />
The line terminator is the character that comes at the end of a row. The lineterminator argument changes the string used to separate rows. By default, the line terminator is a newline.


## 6. What function takes a string of JSON data and returns a Python data structure?

`json.loads()`

## 7. What function takes a Python data structure and returns a string of JSON data?

`json.dumps()`

