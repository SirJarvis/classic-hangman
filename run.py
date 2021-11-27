import random
from words import word_list


def get_word():
    # Function that returns word to game
    word = random.choice(word_list)
    return word.upper()


def play(word):
    # Interactive game function
    word_completion = "_" * len(word)
    guessed = False
    # List that holds the letters that player guessed
    guessed_letters = []
    # List that holds the words that player guessed
    guessed_words = []
    attempt = 8
    # Initial output to guide player when game starts
    print("Let's play Hangman")
    print(display_hangman(attempt))
    print(word_completion)
    print("\n")

    while not guessed and attempt > 0:
        # While loop will run until word is guessed or user rans out of tries
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            # Guessing a letter has length of 1 and contains only characters from alphabet
            if guess in guessed_letters:
                print("Letter has been already guessed", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                attempt -= 1
                guessed_letters.append(guess)
            else:
                print("Congrats", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            # Length of guess equals the length of word and contains only letters
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                attempt -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(display_hangman(attempt))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, word has been guessed. You won")
    else:
        print("Sorry you lost. The word was " + word + ". Better luck next time")


def display_hangman(attempt):
    # Function that shows current level of hangman based of each attempt
    levels = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return levels[attempt]
