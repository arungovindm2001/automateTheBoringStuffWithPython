## 1. What are the two values of the Boolean data type? How do you write them?

**True and False** are the two values of the Boolean data type.<br />
They always start with a capital T or F, with the rest of the word in lowercase.


## 2. What are the three Boolean operators?

and<br />
or<br />
not

## 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

AND
| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
|   0     |   0     |   0    |	
|   0     |   1     |   0    |
|   1     |   0     |   0    |	
|   1     |   1     |   1    |

OR
| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
|   0     |   0     |   0    |	
|   0     |   1     |   1    |
|   1     |   0     |   1    |	
|   1     |   1     |   1    |

NOT
| Input | Output |
|-------| ------ |
|   0   |   1    |	
|   1   |   0    |

## 4. What do the following expressions evaluate to?

#### (5 > 4) and (3 == 5)
False
#### not (5 > 4)
False
#### (5 > 4) or (3 == 5)
True
#### not ((5 > 4) or (3 == 5))
False
#### (True and True) and (True == False)
False
#### (not False) or (not True)
True

## 5. What are the six comparison operators?

| Operator  | Meaning                   |
| --------- | ------------------------- |
|    ==     | Equal to                  |
|    !=     | Not equal to              |
|     <     | Less than                 |
|     >     | Greater than              |
|    <=     | Less than or equal to     |
|    >=     | Greater than or equal to  |

## 6. What is the difference between the equal to operator and the assignment operator?

The  equal to operator **(==)** asks whether two values are the same as each other.<br />
The assignment operator **(=)** puts the value on the right into the variable on the left.

## 7. Explain what a condition is and where you would use one.
Conditions evaluate down to a Boolean value, True or False.<br />
We use a condition whenever we want the program to go to separate ways.<br />
For example, if we want to print 'Hi, Alice', we use a condition to check whether the given input is Alice or not.

## 8. Identify the three blocks in this code:
**spam = 0**<br />
**if spam == 10:**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**print('eggs')**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**if spam > 5:**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**print('bacon')**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**else:**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**print('ham')**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**print('spam')**<br />
**print('spam')**
<br />

The three blocks of code are:

---
if spam == 10:<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('eggs')<br />
&nbsp;&nbsp;&nbsp;&nbsp;if spam > 5:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('bacon')<br />
&nbsp;&nbsp;&nbsp;&nbsp;else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('ham')<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('spam')

---
if spam > 5:<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('bacon')

---

---
else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('ham')<br />

---


## 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

---
spam = int(input())<br />
if spam == 1 :<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('Hello')<br />
elif spam == 2:<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('Howdy')<br />
else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;print('Greetings!')

---

## 10. What keys can you press if your program is stuck in an infinite loop?

You can either press CTRL-C or select Shell ▸ Restart Shell from IDLE’s menu.

## 11. What is the difference between break and continue?

break is used to exit out of a loop's clause.<br />
continue is used to jump the program's execution to the start of a loop.

## 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

All do the same thing.<br />
range(10) ranges from 0 to 9<br />
range(0,10) tells the loop to start from 0 and end at 9.<br />
range(0,10,1) tells the loop to start from 0 with an increment of 1 and end at 9.

## 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Program using a **for loop**

---
for number in range(1,11,1):<br />
&nbsp;&nbsp;&nbsp;&nbsp;print(number)

---
    
Program using a **while loop**

---
number = 1<br />
while number <=10 :<br />
&nbsp;&nbsp;&nbsp;&nbsp;print(number)<br />
&nbsp;&nbsp;&nbsp;&nbsp;number = number + 1
    
---

## 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

spam.bacon()
