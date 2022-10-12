# final copy
# hangman

from random_word import RandomWords


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

hang_man_graphic = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                                   '''

# word_list = ["aardvark", "baboon", "camel"]

#using pip random word generator to get random words

r = RandomWords()
chosen_word = r.get_random_word()
word_length = len(chosen_word)

# Testing code
print(hang_man_graphic+"\n\n")
print(f'The solution is {chosen_word}.') # cheat code

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

player_lives = 6

guessed_letters = []

while not end_of_game:

    pos_found = False

    guess = input("Guess a letter: ").lower()

    guessed_letter_found = False
    for letter in guessed_letters:
        if guess == letter:
            guessed_letter_found = True

    if guessed_letter_found:
        print(f"You have already guessed '{guess}' before. Try a different letter.")
        continue

    guessed_letters.append(guess)
    # Check guessed letter

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            pos_found = True

    print(display)

    if not pos_found:
        player_lives -= 1
        print(f"You have {player_lives} tries left.\n")
        print(stages[player_lives])

    # Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    if player_lives == 0:
        end_of_game = True
        print("You loose.")