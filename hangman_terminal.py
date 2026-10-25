import random

MAX_MISTAKES = 6

WORDS = [
    "PYTHON",
    "COMPUTER",
    "SECURITY",
    "NETWORK",
    "DATABASE",
    "ALGORITHM",
    "DEVELOPER",
    "HANGMAN",
    "SOFTWARE",
    "HARDWARE",
]

HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def display_game(word, guessed_letters, mistakes):
    print(HANGMAN_STAGES[mistakes])

    masked_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )

    print("Word:", masked_word)
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    mistakes = 0

    print("\n=== HANGMAN ===")
    print("Guess the secret word one letter at a time.")

    while mistakes < MAX_MISTAKES:
        display_game(secret_word, guessed_letters, mistakes)

        if set(secret_word) <= guessed_letters:
            print("\nCongratulations! You guessed the word!")
            return

        guess = input("\nEnter a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter one letter from A to Z.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Incorrect! '{guess}' is not in the word.")

    display_game(secret_word, guessed_letters, mistakes)
    print("\nGame over! You used all six mistakes.")
    print(f"The secret word was: {secret_word}")


def main():
    while True:
        play_hangman()

        play_again = input("\nPlay again? (y/n): ").strip().lower()

        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()