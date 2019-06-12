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
    background = pygame.image.load('Drawings/linedpaper.png')
    window.blit(background, (0, 0))
    font = pygame.font.Font('Drawings/IndieFlower.ttf', 90)
    window.blit(font.render('Hangman', True, black), (145, -20))
    noose = pygame.image.load('Drawings/noose.png')
    window.blit(noose, (90, 145))
    for i in range(len(word)):
        blank_line = pygame.image.load('Drawings/blank_line.png')
        window.blit(blank_line, (320 + (i*66) - ((66*(len(word)-1))/2), 619 + ((-1)**i)))
    pygame.display.update()

def correct_guess(guess):
    print('correct!')


def wrong_guess(guess):
    print('wrong')
    head = pygame.image.load('Drawings/head.png')
    window.blit(head, (245, 192))
    pygame.display.update()
    
    body = pygame.image.load('Drawings/body.png')
    window.blit(body, (275, 250))
    pygame.display.update()

    left_arm = pygame.image.load('Drawings/left_arm.png')
    window.blit(left_arm, (237, 258))
    pygame.display.update()

    right_arm = pygame.image.load('Drawings/right_arm.png')
    window.blit(right_arm, (282, 249))
    pygame.display.update()

    left_leg = pygame.image.load('Drawings/left_leg.png')
    window.blit(left_leg, (250, 313))
    pygame.display.update()

    right_leg = pygame.image.load('Drawings/right_leg.png')
    window.blit(right_leg, (282, 313))
    pygame.display.update()


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
