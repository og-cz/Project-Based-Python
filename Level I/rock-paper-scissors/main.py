import src.game as game

def main():
    g = game.Game()
    guesser = game.Guess()
    guess_this = ''

    while g.get_tries() < 3:
        inp = input('Choose either Rock, Paper or Scissors: ')
        guess_this = guesser.randomize()
        if inp in guesser.get_guesses():
            if inp == guess_this:
                return f"You guessed the right answer: {guess_this}"
            else:
                g.tries()
        else:
            print('Only choose between - Rock, Paper or Scissors')
        print('Next Round... you have', (3 - g.get_tries()), 'tries left')
    return f'You lose! the correct answer: {guess_this}'

if __name__ == "__main__":
    result = main()
    print(result)