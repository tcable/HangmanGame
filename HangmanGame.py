import random
# hangman game

# select random word from word_list.txt
f = open("word_list.txt", "r")
words = f.readlines()
f.close()
# make sure the test file isn't empty
try:
    word = words[random.randint(0, len(words)-1)]
except ValueError:
    print("file is empty")
else:
    # remove any trailling return characters (found on all words except the last one in the file)
    if "\n" in word:
        word = word[:-1]
    # print(word)
    charactersremaining = len(word)

    # create * list
    guessed = "*" * charactersremaining
    guessed = list(guessed)

    # make guesses if seven wrong guesses are made lose
    remaining_guesses = 7
    while remaining_guesses > 0:

        guess = input("You have " + str(remaining_guesses) + " guesses remaining.\n" +
                      "".join(guessed) + "\nPlease enter your next guess: ")
        # check to see if the guess is a single character
        if len(guess) > 1:
            print("Please only enter 1 character at a time")
            guess = guess[0]
        # check to see if the guess is lower case and if not convert it
        if guess.isupper():
            guess = guess.lower()
        # check to see if guess is in word
        if guess in word and guess != "":
            # find location of guess in word and update guessed
            x = word.find(guess)
            guessed[x] = guess
            while x > -1:
                x += 1
                x = word.find(guess, x)
                if not x == -1:
                    guessed[x] = guess
        else:
            remaining_guesses -= 1

        # check if all characters guessed correctly
        if not "*" in guessed:
            print("congratulations you win")
            remaining_guesses = -1

    if remaining_guesses == 0:
        print("lose")
