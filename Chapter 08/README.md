## 1. Does PyInputPlus come with the Python Standard Library?

No. We have to download and install it externally from terminal using the command:<br />
`pip install pyinputplus`

## 2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?

`import pyinputplus as pyip` makes it easier to type out functions as `pyip` rather than typing out the whole word `pyinputplus` many times.

## 3. What is the difference between inputInt() and inputFloat()?

`inputInt()` validates the input as Integer and `inputFloat()` validates as Floating-point value.

## 4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?

We limit the input values using min and max, limiting min to 0 and max to 99. The code looks like this.<br />
```
import pyinputplus as pyip
pyip.inputNum(min=0,max=99)
```

## 5. What is passed to the allowRegexes and blockRegexes keyword arguments?

`allowRegexes` and `blockRegexes` take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.

## 6. What does inputStr(limit=3) do if blank input is entered three times?

The code `inputStr(limit=3)` stops execution and  after taking invalid inputs 'limit' number of times. In this case limit is 3.

## 7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?

'hello' is put as the value since blank value is considered as invalid input. Since limit is 3, and blank input is entered three times, the default value 'hello' is put as its value.
