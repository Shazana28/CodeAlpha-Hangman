import random
import json
import os

# List of words
words = ["python", "developer", "hangman", "mobile", "programming", "codealpha"]

# File to store user scores
SCORES_FILE = "hangman_scores.json"

# Load scores
def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    return {}

# Save scores
def save_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f)

# Function to get a random word
def get_random_word():
    return random.choice(words).upper()

# Function to display Hangman stages (visual)
def display_hangman(attempts):
    stages = [
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
        """,
        """
         ------
         |    |
         |
         |
         |
         |
        """
    ]
    return stages[attempts]

# Function to play Hangman
def play_hangman():
    username = input("Enter your name: ")
    scores = load_scores()
    if username not in scores:
        scores[username] = 0  # Initialize score if new player

    word = get_random_word()
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    attempts = 6  # Max incorrect attempts

    print("\nWelcome to Hangman, " + username + "!")
    print("Try to guess the word, one letter at a time.")

    while attempts > 0 and "_" in guessed_word:
        print(display_hangman(attempts))
        print("\nWord: " + " ".join(guessed_word))
        print(f"Incorrect Attempts Left: {attempts}")
        print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            attempts -= 1

    # Game Over
    if "_" not in guessed_word:
        print(f"\n🎉 Congratulations, {username}! You guessed the word: {word} 🎉")
        scores[username] += 10  # Add 10 points for winning
    else:
        print(display_hangman(0))
        print(f"\n💀 Game Over! The correct word was: {word} 💀")

    # Save score
    save_scores(scores)
    print(f"Your Score: {scores[username]}\n")

# Start the game
if __name__ == "__main__":
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break