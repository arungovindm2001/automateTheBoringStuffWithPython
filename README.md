# Automate The Boring Stuff With Python
Contains the answers to the practice questions and the practice projects of the book "Automate the Boring Stuff With Python, 2nd Edition" by Al Sweigart.
## Chapter 1 - Python Basics
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2001/README.md)

## Chapter 2 - Flow Control
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2002/README.md)

## Chapter 3 - Functions
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2003/README.md)<br />
Practice Project - [The Collatz Sequence](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2003/Practice%20Projects/The%20Collatz%20Sequence.py)<br />

Practice Project - [The Collatz Sequence with Input Validation](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2003/Practice%20Projects/The%20Collatz%20Sequence%20with%20Input%20Validation.py)<br />
<br />

To see the step-by step execution of Collatz Sequence [click here](http://pythontutor.com/visualize.html#code=def%20collatz%28number%29%3A%0A%20%20%20%20if%20number%20%25%202%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20number//2%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%203*number%2B1%0A%0Aprint%28'Enter%20number%3A'%29%0Anumber%20%3D%20int%28input%28%29%29%0A%0An%3Dcollatz%28number%29%0Aprint%28n%29%0A%0Awhile%20n-1%20!%3D%200%3A%20%20%20%20%0A%20%20%20%20n%3Dcollatz%28n%29%0A%20%20%20%20print%28n%29%0A&cumulative=false&curInstr=45&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2210%22%5D&textReferences=false)<br />

To see the step-by step execution of Collatz Sequence with Input Validation [click here](http://pythontutor.com/visualize.html#code=def%20collatz%28number%29%3A%0A%20%20%20%20if%20number%20%25%202%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20number//2%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%203*number%2B1%0A%20%20%20%20%0Atry%3A%0A%20%20%20%20print%28'Enter%20number%3A'%29%0A%20%20%20%20number%20%3D%20int%28input%28%29%29%0A%20%20%20%20n%3Dcollatz%28number%29%0A%20%20%20%20print%28n%29%0A%0A%20%20%20%20while%20n-1%20!%3D%200%3A%20%20%20%20%0A%20%20%20%20%20%20%20%20n%3Dcollatz%28n%29%0A%20%20%20%20%20%20%20%20print%28n%29%0A%0Aexcept%20ValueError%3A%0A%20%20%20%20print%28'You%20must%20enter%20an%20integer'%29&cumulative=false&curInstr=46&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2210%22%5D&textReferences=false)

## Chapter 4 - Lists
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2004/README.md)

## Chapter 5 - Dictionaries and Structured Data
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2005/README.md)

## Chapter 6 - Manipulating Strings
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2006/README.md)

## Chapter 7 Pattern Matching with Regular Expressions
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2007/README.md)

## Chapter 8 - Input Validation
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2008/README.md)<br />
Practice Project - [Multiplication Quiz](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2008/Practice%20Projects/Multiplication%20Quiz.py)<br />
Practice Project - [Sandwich Maker](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2008/Practice%20Projects/Sandwich%20Maker.py)

## Chapter 9 - Reading and Writing Files
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2009/README.md)

## Chapter 10 - Organizing Files
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2010/README.md)<br />
Practice Project - [Deleting Unneeded Files](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2010/Practice%20Projects/Deleting%20Unneeded%20Files.py)<br />
Practice Project - [Selective Copy](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2010/Practice%20Projects/Selective%20Copy.py)

## Chapter 11 - Debugging
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2011/README.md)<br />
Practice Project - [Debugging a Coin Toss](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2011/Practice%20Projects/Debugging%20a%20Coin%20Toss.py)

## Chapter 12 - Web Scraping
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2012/README.md)<br />
Practice Project - [2048](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2012/Practice%20Projects/2048.py)<br />
Practice Project - [Command Line Emailer](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2012/Practice%20Projects/CommandLineEmailer.py)

## Chapter 13 - Working with Excel Spreadsheets
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2013/README.md)<br />
Practice Project - [Spreadsheet Cell Inverter](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2013/Practice%20Projects/Spreadsheet%20Cell%20Inverter.py)<br />
Practice Project - [Multiplication Table Maker](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2013/Practice%20Projects/multiplicationTable.py)<br />
Practice Project - [Text Files to Spreadsheet](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2013/Practice%20Projects/sheet2txt.py)<br />
Practice Project - [Spreadsheet to Text Files](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2013/Practice%20Projects/txtToxlsx.py)

## Chapter 14 - Working with Google Sheets
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2014/README.md)<br />
Practice Project - [Converting Spreadsheets to Other Formats](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2014/Practice%20Projects/Converting%20Spreadsheets%20to%20Other%20Formats.py)<br />
Practice Project - [Downloading Google Forms Data](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2014/Practice%20Projects/Downloading%20Google%20Forms%20Data.py)<br />
Practice Project - [Finding Mistakes in a Spreadsheet](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2014/Practice%20Projects/Finding%20Mistakes%20in%20a%20Spreadsheet.py)

## Chapter 15 - Working with PDF and WORD Documents
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2015/README.md)<br />
Practice Project - [PDF Paranoia](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2015/Practice%20Projects/PDFParanoia.py)

## Chapter 16 - Working with CSV Files and JSON Data
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2016/README.md)<br />
Practice Project - [Excel to CSV Converter](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2016/Practice%20Project/Excel-to-CSV%20Converter.py)

## Chapter 17 - Keeping Time, Scheduling Tasks, and Launching Programs
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2017/README.md)<br />
Practice Project - [Prettified Stopwatch](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2017/Practice%20Projects/Prettified%20Stopwatch.py)

## Chapter 18 - Sending Email and Text Messages
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2018/README.md)

## Chapter 19 - Manipulating Images
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2019/README.md)<br />
Practice Project - [Identifying Photo Folders on the Hard Drive](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2019/Practice%20Projects/Identifying-Photo-Folders-on-the-Hard-Drive.py)

## Chapter 20 - Controlling Keyboard and Mouse with GUI Automation
[Practice Questions](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2020/README.md)<br />
Practice Project - [Looking Busy](https://github.com/arungovindm2001/automateTheBoringStuffWithPython/blob/main/Chapter%2020/Practice%20Projects/Looking-Busy.py)
