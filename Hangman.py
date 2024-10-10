import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat cobra '
        'coyote crow deer dog donkey duck eagle fox frog goat '
        'goose lion lizard llama mole monkey mouse '
        'otter owl panda parrot pigeon python rabbit ram rat raven '
        'rhino salmon seal shark sheep skunk sloth snake spider '
        'tiger toad turkey turtle whale wolf '
        'zebra ').split()

def getRandomWord(wordList):
    return random.choice(wordList)

def displayBoard(HANGMANPICS, usedLetters, correctLetters, secretWord):

    print(HANGMANPICS[len(usedLetters)])
    print("Used letters:", ' '.join(usedLetters))

    blanks = ['_'] * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]
    print(' '.join(blanks))

def getGuess(alreadyGuessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in alreadyGuessed:
            return guess
        print("Invalid guess. Try again.")

def playAgain():
    return input("Play again? (yes or no): ").lower().startswith('y')

print("H A N G M A N")

while True:
    usedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameOver = False

    while not gameOver:
        displayBoard(HANGMANPICS, usedLetters, correctLetters, secretWord)
        guess = getGuess(usedLetters + correctLetters)

        if guess in secretWord:
            correctLetters += guess
            if all(letter in correctLetters for letter in secretWord):
                print(f"You've won! The word was '{secretWord}'.")
                gameOver = True
        else:
            usedLetters += guess
            if len(usedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, usedLetters, correctLetters, secretWord)
                print(f"You've lost! The man has been hanged💀\nThe word was '{secretWord}'.")
                gameOver = True

    if not playAgain():
        break
