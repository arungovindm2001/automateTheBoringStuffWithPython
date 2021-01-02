import random
guess = ''
guessToToss = {0:'tails',1:'heads'}
toss = guessToToss[random.randint(0, 1)] # 0 is tails, 1 is heads

while guess not in guessToToss.values():
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

if toss == guess:
    print('You got it!')
else:
    guess = ''
    while guess not in guessToToss.values():
        print('Nope! Guess again!')
        guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
