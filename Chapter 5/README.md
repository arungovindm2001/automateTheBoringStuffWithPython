## 1. What does the code for an empty dictionary look like?

{}

## 2. What does a dictionary value with a key 'foo' and a value 42 look like?

{'foo':42}

## 3. What is the main difference between a dictionary and a list?

Unlike lists, items in dictionaries are unordered.

## 4. What happens if you try to access spam['foo'] if spam is {'bar': 100} ?

Trying to access a key that does not exist in a dictionary will result in a KeyError error message.<br />

```
Traceback (most recent call last):
File "<pyshell#1>", line 1, in <module>
spam['foo']
KeyError: 'foo'
```

## 5. If a dictionary is stored in spam , what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys() ?

`'cat' in spam` searches the keys and values present in the dictionary spam.<br />
`'cat' in spam.keys()` searches only the keys present in the dictionary.

## 6. If a dictionary is stored in spam , what is the difference between the expressions 'cat' in spam and 'cat' in spam.values() ?

`'cat' in spam` searches the keys and values present in the dictionary spam.<br />
`'cat' in spam.values()` searches only the values present in the dictionary.

## 7. What is a shortcut for the following code?
**if 'color' not in spam:**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**spam['color'] = 'black'**

`spam.setdefault('color','black')`

## 8. What module and function can be used to “pretty print” dictionary values?
We import the `pprint` module.<br />
`import pprint`

function is `pprint()`<br />
`pprint.pprint()`
