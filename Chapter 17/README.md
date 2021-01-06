## 1. What is the Unix epoch?

The Unix epoch is a time reference commonly used in programming. It starts at 12 AM on January 1, 1970, Coordinated Universal Time (UTC).

## 2. What function returns the number of seconds since the Unix epoch?

`time.time()`

## 3. How can you pause your program for exactly 5 seconds?

`time.sleep(5)`

## 4. What does the round() function return?

`round()` function rounds a float to the precision you specify.

## 5. What is the difference between a datetime object and a timedelta object?

`datetime` - represents a specific moment in time<br />
`timedelta` - represents a duration of time.<br />
For example:<br />
`datetime.datetime(2019, 10, 31, 0, 0, 0)` represents that moment in time<br />
`datetime.timedelta(days=11, hours=10, minutes=9, seconds=8).total_seconds` represents the number of seconds it will take to reach that moment of time.

## 6. Using the datetime module, what day of the week was January 7, 2019?

`datetime.datetime(2019,1,7).weekday()`<br />
This returns 0 which means Monday since datetime module uses 0 for Monday, 1 for Tuesday, and so on..

## 7. Say you have a function named spam() . How can you call this function and run the code inside it in a separate thread?

```
threadObj = threading.Thread(target=spam)
threadObj.start()
```

## 8. What should you do to avoid concurrency issues with multiple threads?

Things you should keep in mind to avoid concurrency issues:<br />
1. **Never** let multiple threads **read or write the same variables**.
2. When you create a new Thread object, make sure its **target function uses only local variables** in that function.
