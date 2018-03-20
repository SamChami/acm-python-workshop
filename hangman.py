import sys

def main():
    print("Welcome to Hangman")
    if len(sys.argv) > 1:
        createHangman(sys.argv[1])
    else:
        createHangman(getWord())

def getWord():
    return "TEST"

def createHangman(word):
    guesses = 7
    word = createWord("", word)
    while guesses > 0:
        print("You have ", guesses, "guesses remaining.")
        print(displayWord)
        letterGuess = input("Guess a letter ")
        guesses = checkLetter(guesses, word, letterGuess)

def checkLetter(guesses, word, letter):
    if word.find(letter) != -1 and letter != "":
        print("Right!")
        return guesses
    else:
        print("Wrong!")
        return guesses - 1

def winOrLoss():
    return "TEST"

main()
