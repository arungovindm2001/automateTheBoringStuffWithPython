import time, pyperclip, sys

# Display the programs instructions.
print('''
ENTER  - START.
ENTER  - DISPLAY TIME.
Ctrl-C - Quit.
''')

input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        
        input()
        
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        lap = 'lap # '+str(lapNum)+ ':'.ljust(3)+' '+str(totalTime).rjust(5)+' ('+str(lapTime).rjust(6)+')'
        print(lap)
        lapNum += 1
        lastTime = time.time()
        pyperclip.copy(lap)       
except KeyboardInterrupt:
    print('Stopped Successfully')
    sys.exit()
