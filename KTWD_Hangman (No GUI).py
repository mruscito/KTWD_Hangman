# Hangman for Intel KTWD 2019
# by Michael Ruscito
import pygame, sys

# initialize game window
pygame.init()
window_width = 620
window_height = 766
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Intel KTWD Hangman')
clock = pygame.time.Clock()

# initialize writing fonts
title_font = pygame.font.Font('Drawings/IndieFlower.ttf', 90)
letter_font = pygame.font.Font('Drawings/IndieFlower.ttf', 60)
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

# get word for game
def get_word():
    word = 'intel'
    word = word.lower()
    word_list = list(word)
    return word, word_list

# initialize display
def draw_display(word):
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
def correct_guess(word, word_list, guess):
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
def check_guess(word, word_list, guess, wrong_guesses):
    correct = False
    for letter in word:
        if guess == letter:
            correct_guess(word, word_list, guess)
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
def gameover(word, word_list, wrong_guesses, game_over=False):
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
def game_loop(word, word_list):
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
                        wrong_guesses = check_guess(word, word_list, guess, wrong_guesses)
                        game_over = gameover(word, word_list, wrong_guesses)
        pygame.display.update()

main_menu()
while True:
    word_info = get_word()
    word = word_info[0]
    word_list = word_info[1]
    draw_display(word)
    game_loop(word, word_list)
    play_again()

