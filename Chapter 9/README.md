## 1. What is a relative path relative to?

A relative path is relative to the program’s current working directory.

## 2. What does an absolute path start with?

An absolute path, always begins with the root folder.

## 3. What does Path('C:/Users') / 'Al' evaluate to on Windows?

`WindowsPath('C:/Users/Al')`

## 4. What does 'C:/Users' / 'Al' evaluate to on Windows?

Will result in an error since you can't join paths with forward slashes in Windows.

## 5. What do the os.getcwd() and os.chdir() functions do?

`os.getcwd()` - gets the current working directory.<br />
`os.chdir()` - changes the current working directory as given in the parameter.

## 6. What are the . and .. folders?

`.` refers to the current folder.<br />
`..` refers to the parent folder.

## 7. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

`C:\bacon\eggs\` is the dir name.<br />
`spam.txt` is the base name.

## 8. What are the three “mode” arguments that can be passed to the open() function?

The three modes are:<br />
`'r'` - read mode<br />
`'w'` - write mode<br />
`'a'` - append mode

## 9. What happens if an existing file is opened in write mode?

The contents of the file gets erased completely and the file is overwritten again.

## 10. What is the difference between the read() and readlines() methods?

`read()` evaluates the whole content of the file as a single string<br />
`readlines()` evaluates each line as an string element in a list

## 11. What data structure does a shelf value resemble?

Resembles a dictionary.

