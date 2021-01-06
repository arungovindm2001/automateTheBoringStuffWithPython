## 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10 .

`assert spam<10, 'Value of spam is '+str(spam)`

## 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

`assert eggs.lower()!=bacon.lower(),'Variables eggs '+eggs+' and bacon '+bacon+' are the same'`

## 3. Write an assert statement that always triggers an AssertionError .

`assert False, 'This statement always triggers an AssertionError'`

## 4. What are the two lines that your program must have in order to be able to call logging.debug() ?

```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

## 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

## 6. What are the five logging levels?

There are five logging levels.

`DEBUG` - The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.<br />
`INFO` - Used to record information on general events in your program or confirm that things are working at their point in the program.<br />
`WARNING` - Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.<br />
`ERROR` - Used to record an error that caused the program to fail to do something.<br />
`CRITICAL` - The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.

##7. What line of code can you add to disable all logging messages in your program?

`logging.disable()`

## 8. Why is using logging messages better than using print() to display the same message?

Once you’re done debugging, you’ll end up spending a lot of time removing print() calls from your code for each log message. You might even accidentally remove some print() calls that were being used for nonlog messages. If you log messages, you can always disable them later by adding a single call. We can also show or hide log messages easily.

## 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

Step In button will cause the debugger to execute the next line of code and then pause again.<br />
Step Over button will execute the next line of code. If the next line of code is a function call, the Step Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns.<br />
Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function.

## 10. After you click Continue, when will the debugger stop?

Clicking the Continue button will cause the program to execute normally until it terminates or reaches a breakpoint.

## 11. What is a breakpoint?

A breakpoint can be set on a specific line of code and forces the debugger to pause whenever the program execution reaches that line.

## 12. How do you set a breakpoint on a line of code in Mu?

To set a breakpoint in Mu, click the line number in the file editor to cause a red dot to appear, marking the breakpoint.

