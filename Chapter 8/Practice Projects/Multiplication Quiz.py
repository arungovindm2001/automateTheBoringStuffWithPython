import random
import time

for i in range(10):
    a = random.randint(0,9)
    b = random.randint(0,9)
    print(a,'x', b)
    start=time.time()
    mul=a*b
    answer = int(input())
    for j in range(2):
        if answer == mul:
            end=time.time()
            if end-start > 8:
                print('Incorrect')
                break
            print('Correct!')
            time.sleep(1)
            break
        else:
            end=time.time()
            if end-start > 8:
                print('Incorrect')
            else:
                answer=int(input())
    
