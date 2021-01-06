## 1. Briefly describe the differences between the webbrowser , requests , bs4 , and selenium modules.

webbrowser module is used to open a URL in a web browser.<br />
requests module is used to download content from the web.<br />
bs4 module is used to parse HTML.<br />
selenium module is used to control a web browser.

## 2. What type of object is returned by requests.get() ? How can you access the downloaded content as a string value?

A Response Object.<br />
`<class 'requests.models.Response'>`<br />
It has a text attribute which can access the download content as a string value.<br />
`requests.get(url_in_quotes).text`

## 3. What requests method checks that the download worked?

`requests.get(url_in_quotes).raise_for_status()`<br />
Displays nothing if successful but displays error if the download disn't work like this:
```
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "Path\Python\Python37\lib\site-packages\requests\models
.py", line 940, in raise_for_status
raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: <url_in_quotes>
```

## 4. How can you get the HTTP status code of a requests response?

`requests.get(url_in_quotes).status_code`

## 5. How do you save a requests response to a file?

To write the web page to a file, use a for loop with the Response object’s iter_content() method.
```
import requests
siteContent = requests.get(url_in_quotes)
textFile = open('RomeoAndJuliet.txt', 'wb')
for line in siteContent.iter_content(100000):
  textFile.write(line)
playFile.close()
```
This will save the file in the script's directory.

## 6. What is the keyboard shortcut for opening a browser’s developer tools?

**F12** in Chrome and Internet Explorer.<br />
**Ctrl+Shift+C** on Windows and Linux.<br />
**Command+Option+C** on macOS.

## 7. How can you view (in the developer tools) the HTML of a specific element on a web page?

Right click on to the element and select **Inspect Element**

## 8. What is the CSS selector string that would find the element with an id attribute of main ?

`#main`

## 9. What is the CSS selector string that would find the elements with a CSS class of highlight ?

`.highlight`

## 10. What is the CSS selector string that would find all the <div> elements inside another <div> element?

`div div`

## 11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite ?

`button[value='favorite']`

## 12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element `<div>Hello, world!</div>` . How could you get a string 'Hello, world!' from the Tag object?

`spam.getText()`

## 13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem ?

`linkElem.attrs`

## 14. Running import selenium doesn’t work. How do you properly import the selenium module?

`from selenium import webdriver`

## 15. What’s the difference between the find_element_* and find_elements_* methods?

`find_element_*` will return the first matching element.<br />
`find_elements_*` will return a list of all matching elements.

## 16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?

`click()` simulates mouse clicks<br />
`send_keys()` simulates keyboard keys

##17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium ?

Yes there is an easier way.<br />
We can call the `submit()` method on any element within a form. This submits the form.

## 18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium ?
`forward()` - goes one page forward<br />
`back()` - goes one page backward<br />
`refresh()` - refreshes the page
