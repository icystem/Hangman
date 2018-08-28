import random

def get_word():
    with open('word.txt') as f:
        words = open("word.txt").readlines()
        happyface = random.choice(words).upper()
        print (happyface)
        return happyface

def check(word,guesses,guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            matches += 1

    if matches > 1:
        print('Yes! The word contains',matches,'"' + guess + '"' + 's')
    elif matches == 1:
        print('Yes! The word contains the letter "' + guess + '"')
    else:
        print('Sorry. The word does not contain the letter "' + guess + '"')

    return status

def main():
    word = get_word()
    guesses = []
    guessed = False
    print('The word contains',len(word),'letters.')
    while not guessed:
        text = 'Please enter one letter or a {}-letter word. '.format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('You already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guesses, guess)
            if result == word:
                guessed = True

            else:
                print(result)
        else:
            print('Invalid entry.')

    print('Yes, the word is', word + '! You got it in', len(guesses),
          'tries.')



main()