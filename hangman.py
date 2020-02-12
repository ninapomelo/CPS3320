import random
words = ["hangout", "python", "cat", "rabbit"]  
lives_remaining = 6    
guessed_letters = ''

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('Great Job ! ')
            break
        if lives_remaining == 0:
            print('The word is: ' + word)
            break

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]

def get_guess(word):
    print_word(word)
    print('Remain chances ' + str(lives_remaining))
    guess = input('Enter a word： ')
    return guess

def print_word(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    print(display_word)

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():   
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True

play()