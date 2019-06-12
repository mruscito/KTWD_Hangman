# Hangman for Intel KTWD 2019
import pygame, sys

word = 'hangman'

# initialize window
pygame.init()
window_width = 620
window_height = 766
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Intel KTWD Hangman')
clock = pygame.time.Clock()

# RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# initialize display
def draw_display():
    background = pygame.image.load('linedpaper.png')
    window.blit(background, (0,0))
    for letter in word:
        pygame.draw.line(window, black, (90, 80), (200,80), 5)
    pygame.display.update()

def correct_guess(guess):
    print('correct!')


def wrong_guess(guess):
    print('wrong')


def check_guess(guess):
    correct = False
    for letter in word:
        if guess == letter:
            correct_guess(guess)
            correct = True
    if correct == False:
        wrong_guess(guess)
    return

def game_loop():
    while True:
        
        for event in pygame.event.get():
            
            # quit game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess = event.unicode
                
                if guess.isalpha():
                    check_guess(guess)

                print(guess)

draw_display()
game_loop()
