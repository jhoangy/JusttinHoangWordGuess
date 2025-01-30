import random
words = {"able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"}
wordsList = list(words)

def selectWord():
    return random.choice(wordsList)


def checkGuess(guess, secret):
    if guess == secret:
        return "You got it! Amazing!", True
    else:
        return "Wrong guess! Try again", False

def guessGame():
    word = selectWord()
    maxAttempts = 5
    attempts = 0
    win = False
    print("Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess:")
    guess = input()
    while True:
        message, win = checkGuess(guess, word)
        print(message)
        if win:
            break
        if guess in words:
            attempts += 1
        print(f"You have ({maxAttempts - attempts} left)")
        if attempts == maxAttempts:
            print("You're out of turns, game over!")
            break
        guess = input()
if __name__ == "__main__":
    guessGame()