## 1. What are escape characters?

An escape character lets you use characters that are otherwise impossible to put into a string. It consists of a backslash ( \ ) followed by the character you want to add to the string.

## 2. What do the \n and \t escape characters represent?

`\n` - New Line<br />
`\t` - Tab

## 3. How can you put a \ backslash character in a string?

`\\`

## 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

The string is enclosed in double quotes. The string can't be closed with a single quote character.

## 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

We use multiline strings to print the string as it is.<br />
For example:<br />
```
print('''amFOSS
bi0s''')
```
This will result in<br />
```
amFOSS
bi0s
```

## 6. What do the following expressions evaluate to?
#### 'Hello, world!'[1]

`'H'`

#### 'Hello, world!'[0:5]

`'Hello'`

#### 'Hello, world!'[:5]

`'Hello'`

#### 'Hello, world!'[3:]

`'lo, world!'`

## 7. What do the following expressions evaluate to?
#### 'Hello'.upper()

`'HELLO'`

#### 'Hello'.upper().isupper()

`True`

#### 'Hello'.upper().lower()

`False`

## 8. What do the following expressions evaluate to?
#### 'Remember, remember, the fifth of November.'.split()

`['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']`

#### '-'.join('There can be only one.'.split())

`'There-can-be-only-one.'`

## 9. What string methods can you use to right-justify, left-justify, and center a string?

To right justify, we use `<string-name>.rjust(<spaces>)`<br />
To left-justify, we use `<string-name>.ljust(<spaces>)`<br />
To center, we use `<string-name>.center(<space>)`

## 10. How can you trim whitespace characters from the beginning or end of a string?

To trim whitespaces from the beginning, we use `<string-name>.lstrip()`<br />
To trim whitespaces from the end, we use `<string-name>.rstrip()`
