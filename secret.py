import random

def secret():
    secret = random.randint(0, 99)
    prompt = 'What is your guess?\n'
    guess = int(input(prompt))
    n = 0
    while guess != secret:
        if guess > secret:
            print('That is too high.')
        else:
            print('That is too low.')
        guess = int(input(prompt))
        n = n + 1
    print('Congratulations!')
    print('Number of guesses:', n)
    print(comment(n))

def comment(n):
    if n == 1:
        return 'Perfect guess!'
    elif 1 < n < 5:
        return 'Nice work!'
    elif n == 5:
        return 'Took you long enough!'
    elif n > 5:
        return 'Better luck next time!'

def game():
    return secret()

game()
