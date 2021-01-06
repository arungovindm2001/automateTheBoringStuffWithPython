## 1. How can you trigger PyAutoGUI’s fail-safe to stop a program?

To stop a program, quickly slide the mouse to one of the four corners of the screen.

## 2. What function returns the current resolution() ?

`pyautogui.size()` returns the current resolution as a tuple with two integers - the width and the height of the screen

## 3. What function returns the coordinates for the mouse cursor’s current position?

`pyautogui.position()`

## 4. What is the difference between pyautogui.moveTo() and pyautogui.move() ?

The `pyautogui.move()` function moves the mouse cursor relative to its current position.<br />
The `pyautogui.moveTo()` function will instantly move the mouse cursor to a specified position on the screen.

## 5. What functions can be used to drag the mouse?

```
pyautogui.dragTo()
pyautogui.drag()
```

## 6. What function call will type out the characters of "Hello, world!" ?

`pyautogui.typewrite("Hello, world!")`

## 7. How can you do keypresses for special keys such as the keyboard’s left arrow key?

`pyautogui.press('left')`

## 8. How can you save the current contents of the screen to an image file named screenshot.png?

`pyautogui.screenshot('screenshot.png')`

## 9. What code would set a two-second pause after every PyAutoGUI function call?

`pyautogui.PAUSE = 2`

## 10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?

Selenium. There are high chances of getting bugs if you use PyAutoGUI.

## 11. What makes PyAutoGUI error-prone?

PyAutoGUI clicks and types blindly. It cannot easily find out if it’s clicking and typing into the correct windows. If any pop-up windows or errors comes unexpectedly, it can lead the program to do something else forcing you to shut it down.

## 12. How can you find the size of every window on the screen that includes the text Notepad in its title?

`pyautogui.getWindowsWithTitle('Notepad')`

## 13. How can you make, say, the Firefox browser active and in front of every other window on the screen?

`pyatuogui.getWindowsWithTitle('Firefox').active()`

