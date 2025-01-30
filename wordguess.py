import random
words = {"able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"}
wordsList = list(words)

def selectWord():
    return random.choice(wordsList)


def checkGuess(guess, secret):
    if guess == secret:
        return True
    else:
        return False

def guessGame():
    word = selectWord()
    guess = input()
    while not checkGuess(guess, word):
        guess = input()
    return "You Win"
if __name__ == "__main__":
    
    print(guessGame())