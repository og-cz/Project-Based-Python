import random

score = 20
random_num = random.randint(0, 100)

while score > 0:
    guess = int(input('guess the number between 1 to 100 (press Q to quit): '))
    if guess == random_num:
        break
    if str(guess).lower() == 'q':
        break
    score -= 1

    if guess > random_num:
        print('hint: try to lower your guess')
    elif guess < random_num:
        print("hint: try to increase your guess")

print('you got a score of', score, 'out of 20')