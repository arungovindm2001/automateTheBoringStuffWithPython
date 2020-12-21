def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3*number+1
    
try:
    print('Enter number:')
    number = int(input())
    n=collatz(number)
    print(n)

    while n-1 != 0:    
        n=collatz(n)
        print(n)

except ValueError:
    print('You must enter an integer')
