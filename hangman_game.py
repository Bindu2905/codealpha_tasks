import random  # Importing random module to select a random word

# List of predefined words
words = ["apple", "banana", "orange", "grape", "mango"]

# Randomly choose one word from the list
chosen_word = random.choice(words)

# List to store the letters guessed by the player
guessed_letters = []

# Number of attempts allowed
attempts = 6

print("Welcome to Hangman!")

# Run the loop until attempts run out
while attempts > 0:
    display_word = ""

    # Build the display word with guessed letters and underscores
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    # Show the current status of the word
    print("Word:", display_word)

    # Check if the whole word is guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    # Take a guess from the user
    guess = input("Guess a letter: ").lower()

    # Check if the letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check if the guess is incorrect
    if guess not in chosen_word:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")
    else:
        print("Good guess!")

# If attempts run out, reveal the word
if attempts == 0:
    print("You ran out of attempts! The word was:", chosen_word)
