import random
from art import stages, logo
from hangman_words import word_list

print(logo)

# Choose a word randomly from the list 
chosen_word = random.choice(word_list)

# Test
# print(f"The solution is {chosen_word}.")

lives = 6

# List to keep track of guessed letters
guessed_letter = []

# List that displays underscores for the hidden letters
display = []
for letter in chosen_word:
    display.append('_')
print(display)

game_over = False

while game_over == False:
    # Check if all the letters have been guessed
    if '_' not in display:
        game_over = True
        print("You won!")
    # Check if the player has run out of lives
    elif lives == 0:
        game_over = True
        print('You lose.')
    else:
        guess = input("Guess a letter: ").lower()
        # Check if the letter has already been guessed
        if guess in guessed_letter:
            print(f"You have already guessed {guess}.")
            continue
        guessed_letter.append(guess) # add that letter in the guessed letters list

        # Check if the letter is not in the chose word
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word")
            if lives == 1:
                print(f"Wrong guess! You have {lives} life left.")
            else:
                print(f"Wrong guess! You have {lives} lives left.")
            print(stages[lives])
        else:
            # Update the display with the correct guessed letter
            for i in range(len(chosen_word)):                
                if chosen_word[i] == guess:
                    display[i] = guess
            print(display)
        