import random
def choose_word():
    words = ["kim namjoon","kim seokjin","min yoongi","jung hoseok","park jimin", "kim taehyung" ,"jeon jungkook"]
    return random.choice(words)
def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def play_word_jumble():
    original_word = choose_word()
    jumbled_word = jumble_word(original_word)

    print("Welcome to Word Jumble!")
    print("Unscramble the letters to form a meaningful word.")

    print(f"Jumbled Word: {jumbled_word}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print("Congratulations! You've guessed the word correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! Try again. Remaining attempts: {attempts}")
            else:
                print(f"Sorry, you're out of attempts. The correct word was '{original_word}'.")
if __name__ == "__main__":
    play_word_jumble()