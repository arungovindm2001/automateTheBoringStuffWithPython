## 1. What is [] ?

[] refers to an empty list.

## 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam ? (Assume spam contains [2, 4, 6, 8, 10] .)

We use the function `insert` to add a value in between elements in a list.<br />

Syntax of `insert` is `<List-name>.insert(position,value)`<br />

`spam.insert(1,'hello')`

## For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'] .

| a | b | c | d |
|---|---|---|---|
| 0 | 1 | 2 | 3 |
| -4|-3 |-2 |-1 |

#### 3. What does spam[int(int('3' * 2) // 11)] evaluate to?

Order of precedence is<br />
int('3'*2) --> 6<br />
int(6//11) --> 0<br />
spam[0]<br />
Therefore, it evaluates to spam[0] which is 'a'.

#### 4. What does spam[-1] evaluate to?

'd'

#### 5. What does spam[:2] evaluate to?

['a','b']

## For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True] .

| 3.14 | 'cat' | 11 | 'cat' | True |
|------|-------|----|-------|------|
|   0  |   1   | 2  |   3   |   4  |
|  -5  |  -4   | -3 |  -2   |  -1  | 

#### 6. What does bacon.index('cat') evaluate to?

3

#### 7. What does bacon.append(99) make the list value in bacon look like?

[3.14,'cat', 11, 'cat', True, 99]

#### 8. What does bacon.remove('cat') make the list value in bacon look like?

`bacon.remove('cat')` will remove the first 'cat' with the index number 1.<br />
So bacon will be [3.14, 11, 'cat', True, 99]

## 9. What are the operators for list concatenation and list replication?

For list concatenation, we use the addition `+` operator .<br />

`newlist = newlist+oldlist`<br/ >

For list replication, we use `copy` for lists or `deepcopy` for lists including lists inside them.<br />
`newlist = copy.copy(oldlist)`<br />
`newlist = copy.deepcopy(oldlist)`<br />

If we want to store a new list in the old list's id, we use `=` operator.<br />
`newlist = oldlist`

## 10. What is the difference between the append() and insert() list methods?

append() method adds an element at the end of the list.<br />
insert() method adds an element at the position we provide in the list.<br />

Consider a list<br />
`>>>list = [1,2,3,4,5]`
<br />
Using append()<br />
```
>>>list.append(6)
>>>list
[1,2,3,4,5,6]
```
Using insert()<br />
```
>>>list.insert(0,0)
>>>list
[0,1,2,3,4,5]
```

## 11. What are two ways to remove values from a list?

`del()`<br />
`remove()`<br />

`del()` method removes values based on their index values.<br />
`remove()` method removes values based on their value names.<br />

```
>>>list = ['cats','dogs','rabbits']
```
Using del() method<br />
```
>>>list.del(1)
>>>list
['cats','rabbits']
```
Using remove() method<br />
```
>>>list.remove('cats')
>>>list
['dogs','rabbits']
```

## 12. Name a few ways that list values are similar to string values.

Strings, like lists, represent ordered sequence of values. They also have indexing, slicing and using them with `for` loops, with `len()` and `in` and `not in`operators.

Consider a string 'amFOSS'. We can represent the string like this (like in lists):

|a|m|F|O|S|S|
|-|-|-|-|-|-|
|0|1|2|3|4|5|
|-6|-5|-4|-3|-2|-1|

```
>>>string = 'amFOSS'
>>>string[0]
'a'
>>>string[0:2]
'am'
>>>for i in string:
      print(i)
a
m
F
O
S
S
>>>len(string)
6
>>>'FOSS' in string
True
>>>'bi0s' not in string
True
```

## 13. What is the difference between lists and tuples?

Lists are mutable while tuples are immutable ie. tuples cannot have their values modified, appended or removed while lists can.<br />
Tuples are typed with parenthesis (), while lists are typed with square brackets [].

## 14. How do you type the tuple value that has just the integer value 42 in it?

We type 42 along with a comma (,) in parenthesis. If we don't provide the comma, Python will take it as a string.<br />
`(42,)`

## 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

We can convert list to tuple and vice-versa by typing the data type we want it to be along with parenthesis and the name inside it.<br />

```
list(<tuplename>)
tuple(<listname>)
```
## 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

Variables store references to list values.

## 17. What is the difference between copy.copy() and copy.deepcopy() ?

The `copy.copy()` function will copy the list (not the lists inside it) to another location.<br />
The `copy.deepcopy()` function will copy the list as well as lists inside it to another location.
