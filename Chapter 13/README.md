## 1. What does the openpyxl.load_workbook() function return?

`openpyxl.load_workbook(<filename>)` returns a Workbook object.<br />
For example: `<openpyxl.workbook.workbook.Workbook object at 0x7f3cd5026790>`<br />
where 0x7f3cd5026790 refers to the id

## 2. What does the wb.sheetnames workbook attribute contain?

It contains a list of all the sheet names of the workbook.

## 3. How would you retrieve the Worksheet object for a sheet named 'Sheet1' ?

`openpyxl.load_workbook(<workbook name>)['Sheet1']`

## 4. How would you retrieve the Worksheet object for the workbook’s active sheet?

`openpyxl.load_workbook(<workbook name>).active`

## 5. How would you retrieve the value in the cell C5?

`sheet['C5']`

## 6. How would you set the value in the cell C5 to "Hello" ?

`sheet['C5'].value = "Hello"`

## 7. How would you retrieve the cell’s row and column as integers?

`cell.row` - returns cell's row as an integer
`cell.column` - returns cell's column as an integer

## 8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?

`sheet.max_column` and `sheet.max_row` attributes hold the highest number of column and row respectively. They are stored as integer data type.

## 9. If you needed to get the integer index for column 'M' , what function would you need to call?

`column_index_from_string('M')`

## 10. If you needed to get the string name for column 14 , what function would you need to call?

`get_column_letter(14)`

## 11. How can you retrieve a tuple of all the Cell objects from A1 to F1?

`sheet['A1':'F1']`

## 12. How would you save the workbook to the filename example.xlsx?

`openpyxl.load_workbook(<workbook name>).save('example.xlsx')`

## 13. How do you set a formula in a cell?

Excel formulas, which begin with an equal sign, can configure cells to contain values calculated from other cells.<br />
For example: `sheet['B9'] = '=SUM(B1:B8)'`<br />
=SUM(B1:B8) will store the sum of all the values containing in B1 till B8 in cell B9.

## 14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?

pass the `data_only` keyword as `True` along with the filename inside `load_workbook()` function arguments.<br />
For example: `openpyxl.load_workbook(<workbook name>,data_only=True)`

## 15. How would you set the height of row 5 to 100?

`sheet.row_dimensions[5].height = 100`

## 16. How would you hide column C?

`sheet.column_dimensions['C'].hidden = True`

## 17. What is a freeze pane?

Freeze panes are rows or columns that always appear on the screen. It doesn't matter how much we scroll down. They are used as headers.

## 18. What five functions and methods do you have to call to create a bar chart?
```
openpyxl.chart.Reference()
openpyxl.chart.Series() 
openpyxl.chart.BarChart()
chartObj.append(seriesObj)
add_chart()
```
