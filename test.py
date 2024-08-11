import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)

print(f"The solution is {chosen_word}.")

lives = 6

display = ['_'] * len(chosen_word)

print(display)

game_over = False

while not game_over:
    if '_' not in display:
        game_over = True
        print("You won!")
    elif lives == 0:
        game_over = True
        print("You lose!")
    else:
        guess = input("Guess a letter: ").lower()

        if guess not in chosen_word:
            lives -= 1
            print(f"Wrong guess! You have {lives} lives left.")
        else:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
            print(display)
