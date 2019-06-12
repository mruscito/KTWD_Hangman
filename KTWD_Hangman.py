# Hangman for Intel KTWD 2019
import pygame, sys

word = 'hangman'

# initialize window
pygame.init()
window_width = 620
window_height = 766
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Intel KTWD Hangman')
title_font = pygame.font.Font('Drawings/IndieFlower.ttf', 90)
letter_font = pygame.font.Font('Drawings/IndieFlower.ttf', 60)
clock = pygame.time.Clock()

# RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# initialize display
def draw_display():
    background = pygame.image.load('Drawings/linedpaper.png')
    window.blit(background, (0, 0))
    window.blit(title_font.render('Hangman', True, black), (145, -20))
    noose = pygame.image.load('Drawings/noose.png')
    window.blit(noose, (90, 145))
    for i in range(len(word)):
        blank_line = pygame.image.load('Drawings/blank_line.png')
        window.blit(blank_line, (320 + (i*66) - ((66*(len(word)-1))/2), 619 + ((-1)**i)))

def correct_guess(guess):
    for occurance in range(len(word)):
        if word.find(guess, occurance) != -1:
            window.blit(letter_font.render(guess, True, black), (325 + (word.find(guess, occurance)*66) - ((66*(len(word)-1))/2), 555 + ((-1)**word.find(guess, occurance))))


def wrong_guess(guess, wrong_guesses):
    if wrong_guesses == 1:
        head = pygame.image.load('Drawings/head.png')
        window.blit(head, (245, 192))
    if wrong_guesses == 2:
        body = pygame.image.load('Drawings/body.png')
        window.blit(body, (275, 250))
    if wrong_guesses == 3:
        left_arm = pygame.image.load('Drawings/left_arm.png')
        window.blit(left_arm, (237, 258))
    if wrong_guesses == 4:
        right_arm = pygame.image.load('Drawings/right_arm.png')
        window.blit(right_arm, (282, 249))
    if wrong_guesses == 5:
        left_leg = pygame.image.load('Drawings/left_leg.png')
        window.blit(left_leg, (250, 313))
    if wrong_guesses == 6:
        right_leg = pygame.image.load('Drawings/right_leg.png')
        window.blit(right_leg, (282, 313))


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

def game_loop():
    game_over = False
    wrong_guesses = 0
    guesses = []
    while not game_over:
        
        for event in pygame.event.get():
            
            # quit game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess = event.unicode
                
                if guess.isalpha():
                    guesses.append(guess)
                    wrong_guesses = check_guess(guess, wrong_guesses)
                    
        pygame.display.update()

while True:
    draw_display()
    game_loop()
