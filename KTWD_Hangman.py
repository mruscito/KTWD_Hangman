# Hangman for Intel KTWD 2019
# by Michael Ruscito
import pygame, sys, random, tkinter as tk
from tkinter import messagebox

# random words
random_words = ['intel', 'computer', 'drive', 'power', 'memory', 'cpu', 'wonderful', 'genuis', 'keyboard', 'future', 'monitor', 'internet', 'gigabyte', 'data', 'program'
                'java', 'python', 'laptop', 'encrypt', 'flash', 'hacker']

# use GUI to get word for game from user
def make_word():
    global word
    word = submit.get()
    if check.get() == 1:
        word = random.choice(random_words)
    word = word.lower()
    global word_list
    word_list = list(word)
    root.destroy()

def use_random():
    if check.get() == 1:
        submit.config(state=tk.DISABLED)
    elif check.get() == 0:
        submit.config(state=tk.NORMAL)

def get_word():
    global root
    root = tk.Tk()
    root.title('Intel KTWD Hangman')
    root.geometry('300x80')
    entry_label = tk.Label(root, text='Enter a word:')
    entry_label.grid(column=0, row=0)
    global submit
    submit = tk.Entry(root)
    submit.grid(column=1, row=0)
    check_label = tk.Label(root, text='Use a random word:')
    check_label.grid(column=0, row=1)
    global check
    check = tk.IntVar()
    checkbox = tk.Checkbutton(root, variable=check, command=use_random)
    checkbox.grid(column=1, row=1)
    play_button = tk.Button(root, text='Play', command=make_word)
    play_button.grid(column=1, row=2)
    root.mainloop()

def word_error(bad_word=False):
    if len(word) > 9:
        messagebox.showerror('Error', 'Please enter a shorter word.\n9 character maximum.')
        bad_word=True
    if not word.isalpha():
        messagebox.showerror('Error', 'Only letters are allowed.\nNo numbers, spaces, or special characters.')
        bad_word=True
    return bad_word

# initialize game window
def initialize_game():
    pygame.init()
    window_width = 620
    window_height = 766
    global window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Intel KTWD Hangman')
    clock = pygame.time.Clock()

# initialize writing fonts
    global title_font
    title_font = pygame.font.Font('Drawings/IndieFlower.ttf', 90)
    global letter_font
    letter_font = pygame.font.Font('Drawings/IndieFlower.ttf', 60)
    global small_font
    small_font = pygame.font.Font('Drawings/IndieFlower.ttf', 20)

# RGB colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (50, 205, 50)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (148 ,0, 211)

# main menu opens before game starts
def main_menu():
    background = pygame.image.load('Drawings/linedpaper.png')
    window.blit(background, (0, 0))
    hangman = pygame.image.load('Drawings/hangman.png')
    window.blit(hangman, (180, 446))
    window.blit(title_font.render('Intel', True, blue), (230, 52))
    window.blit(title_font.render('K', True, green), (200, 172))
    window.blit(title_font.render('T', True, red), (234, 172))
    window.blit(title_font.render('W', True, yellow), (295, 172))
    window.blit(title_font.render('D', True, purple), (350, 172))
    window.blit(title_font.render('Hangman', True, black), (145, 292))
    window.blit(small_font.render('Press any key to play', True, black), (200, 720))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

# initialize display
def draw_display():
    background = pygame.image.load('Drawings/linedpaper.png')
    window.blit(background, (0, 0))
    intel = pygame.image.load('Drawings/intel_logo.png')
    window.blit(intel, (542, 722))
    window.blit(title_font.render('Hangman', True, black), (145, -20))
    noose = pygame.image.load('Drawings/noose.png')
    window.blit(noose, (90, 145))
    for i in range(len(word)):
        blank_line = pygame.image.load('Drawings/blank_line.png')
        window.blit(blank_line, (320 + (i*66) - ((66*(len(word)-1))/2), 619 + ((-1)**i)))

# display letters for a correct guess
def correct_guess(guess):
    for occurance in range(len(word)):
        if word.find(guess, occurance) != -1:
            window.blit(letter_font.render(guess, True, black), (325 + (word.find(guess, occurance)*66) - ((66*(len(word)-1))/2), 555 + ((-1)**word.find(guess, occurance))))
    while guess in word_list:
            word_list.remove(guess)

# draw hangman for a wrong guess
def wrong_guess(guess, wrong_guesses):
    if wrong_guesses == 1:
        head = pygame.image.load('Drawings/head.png')
        window.blit(head, (245, 192))
        window.blit(letter_font.render(guess, True, black), (424, 141))
    if wrong_guesses == 2:
        body = pygame.image.load('Drawings/body.png')
        window.blit(body, (275, 250))
        window.blit(letter_font.render(guess, True, black), (490, 141))
    if wrong_guesses == 3:
        left_arm = pygame.image.load('Drawings/left_arm.png')
        window.blit(left_arm, (237, 258))
        window.blit(letter_font.render(guess, True, black), (424, 221))
    if wrong_guesses == 4:
        right_arm = pygame.image.load('Drawings/right_arm.png')
        window.blit(right_arm, (282, 249))
        window.blit(letter_font.render(guess, True, black), (490, 221))
    if wrong_guesses == 5:
        left_leg = pygame.image.load('Drawings/left_leg.png')
        window.blit(left_leg, (250, 313))
        window.blit(letter_font.render(guess, True, black), (424, 301))
    if wrong_guesses == 6:
        right_leg = pygame.image.load('Drawings/right_leg.png')
        window.blit(right_leg, (282, 313))
        window.blit(letter_font.render(guess, True, black), (490, 301))
        dead = pygame.image.load('Drawings/dead.png')
        window.blit(dead, (260, 208))

# check if the guessed letter is in the word
def check_guess(guess, wrong_guesses):
    correct = False
    for letter in word:
        if guess == letter:
            correct_guess(guess)
            correct = True
    if correct == False:
        wrong_guesses += 1
        wrong_guess(guess, wrong_guesses)
    return wrong_guesses

# check if the current guess was already guessed previously
def previous_guess(guess, old_guesses, new_guess=True):
    for old_guess in old_guesses:
        if guess == old_guess:
            new_guess = False
    return new_guess

# determine if the player won or lost
def gameover(wrong_guesses, game_over=False):
    if wrong_guesses == 6:
        game_over = True
        window.blit(title_font.render('You Lose', True, red), (145, 432))
        for letter in word_list:
            for occurance in range(len(word)):
                if word.find(letter, occurance) != -1:
                    window.blit(letter_font.render(letter, True, red), (325 + (word.find(letter, occurance)*66) - ((66*(len(word)-1))/2), 555 + ((-1)**word.find(letter, occurance))))
    elif len(word_list) == 0:
        game_over = True
        window.blit(title_font.render('You Win!', True, green), (145, 432))
        if wrong_guesses > 0:
            smile = pygame.image.load('Drawings/smile.png')
            window.blit(smile, (261, 210))
    return game_over

# allow player to play again
def play_again():
    window.blit(small_font.render('Press any key to play again', True, black), (180, 720))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

# main loop
def game_loop():
    game_over = False
    wrong_guesses = 0
    old_guesses = []
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                guess = event.unicode
                if guess.isalpha():
                    guess = guess.lower()
                    new_guess = previous_guess(guess, old_guesses)
                    old_guesses.append(guess)
                    if new_guess == True:
                        wrong_guesses = check_guess(guess, wrong_guesses)
                        game_over = gameover(wrong_guesses)
        pygame.display.update()

# run the game
while True:
    get_word()
    bad_word = word_error()
    while bad_word == True:
        get_word()
        bad_word = word_error()
    initialize_game()
    main_menu()
    draw_display()
    game_loop()
    play_again()
