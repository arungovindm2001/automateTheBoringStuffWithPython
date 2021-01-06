## 1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?

`PyPDF2.PdfFileReader(open(<PDF filename>, 'rb'))`

## 2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?

`PdfFileReader()` is opened in **read-binary** mode (rb for short)<br />
`PdfFileWriter()` is opened in **write-binary** mode (wb for short)

## 3. How do you acquire a Page object for page 5 from a PdfFileReader object?

`PdfFileReader.getPage(4)`
We put page 4 as the first page starts from 0, second from 1 and so on..

## 4. What PdfFileReader variable stores the number of pages in the PDF document?

`PdfFileReader.numPages`

## 5. If a PdfFileReader object’s PDF is encrypted with the password swordfish , what must you do before you can obtain Page objects from it?

We have to first decrypt the file to access its Page objects.
`PdfFileReader.decrypt('swordfish')`

## 6. What methods do you use to rotate a page?

`rotateClockwise()` - Used to rotate a page clockwise. We pass one of the integers **90** , **180** , or **270** to it so to specify the degree in which they rotate.<br />
`rotateCounterClockwise()` - Used to rotate a page counterclockwise. We pass one of the integers **90** , **180** , or **270** to it so to specify the degree in which they rotate.

## 7. What method returns a Document object for a file named demo.docx?

`docx.Document('demo.docx')`

## 8. What is the difference between a Paragraph object and a Run object?

A Paragraph object takes the paragraphs of a document.<br />
A Run object refers to the group of same type of characters within a paragraph.

## 9. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc ?

`doc.paragraphs`

## 10. What type of object has bold , underline , italic , strike , and outline variables?

A Run object

## 11. What is the difference between setting the bold variable to True , False , or None ?

`True` - makes the Run object bolded<br />
`False` - makes the Run object not bolded<br />
`None` - uses the style's bold settings

## 12. How do you create a Document object for a new Word document?

`docx.Document()`

## 13. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc ?

`doc.add_paragrapgh('Hello, there!')`

## 14. What integers represent the levels of headings available in Word documents?

0, 1, 2, 3, 4<br />
0 is the main heading and 4 is the lowest sub-heading

