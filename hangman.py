import random

def choose_word(mode):
    easy_words = ["dog", "sun", "hat", "pen", "ice"]
    medium_words = ["apple", "tiger", "plant", "chair", "robot"]
    hard_words = ["python", "crystal", "journey", "hangman", "complex"]

    if mode == "easy":
        return random.choice(easy_words)
    elif mode == "medium":
        return random.choice(medium_words)
    elif mode == "hard":
        return random.choice(hard_words)
    else:
        print("Invalid mode, defaulting to 'medium'")
        return random.choice(medium)

def play_hangman():

    print("\nChoose mode: Easy / Medium / Hard")
    mode = input("Enter mode: ").lower()

    word = choose_word(mode)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print(f"\n🎮 Welcome to Hangman - {mode.capitalize()} Mode!")
    
    while incorrect_guesses < max_incorrect and "_" in guessed_word:
        print("\nWord: " + " ".join(guessed_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print(f"Remaining tries: {max_incorrect - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

    
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("❌ Wrong guess.")
            incorrect_guesses += 1

    
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n don't worry! You'll get it next time. The word is:", word)
while True:
    play_hangman()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing . Goodbye!")
        break
