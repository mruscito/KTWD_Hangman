import pygame, sys, random

random_words = ['intel', 'computer', 'drive', 'power', 'memory', 'cpu', 'wonderful', 'genuis', 'keyboard', 'future', 'monitor', 'internet', 'gigabyte', 'data', 'program',
                'java', 'python', 'laptop', 'encrypt', 'flash', 'hacker', 'chip', 'code', 'icon', 'app', 'phone', 'tech', 'keyboard', 'mouse', 'speed', 'diode', 'logic',
                'electric', 'science', 'engineer', 'core', 'plug', 'charge', 'physics', 'fun', 'google', 'learn', 'email', 'screen', 'webcam', 'shock', 'voltage','current']

class Hangman():

    @staticmethod
    def test():
        print('You imported the Hangman module correctly!')

    @staticmethod
    def random_word():
        word = random.choice(random_words)
        return word

    @staticmethod
    def initialize():
        pygame.init()
        window_width = 620
        window_height = 766
        global window
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Intel KTWD Hangman')
        clock = pygame.time.Clock()
        global title_font
        title_font = pygame.font.Font('Drawings/IndieFlower.ttf', 90)
        global letter_font
        letter_font = pygame.font.Font('Drawings/IndieFlower.ttf', 60)
        global small_font
        small_font = pygame.font.Font('Drawings/IndieFlower.ttf', 20)

    @staticmethod
    def main_menu(black=(0,0,0), red=(255,0,0), green=(50,205,50), blue=(0,0,255), yellow=(255,255,0), purple=(148 ,0, 211)):
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

    @staticmethod
    def draw_noose(color=(0,0,0)):
        background = pygame.image.load('Drawings/linedpaper.png')
        window.blit(background, (0, 0))
        intel = pygame.image.load('Drawings/intel_logo.png')
        window.blit(intel, (542, 722))
        window.blit(title_font.render('Hangman', True, color), (145, -20))
        noose = pygame.image.load('Drawings/noose.png')
        window.blit(noose, (90, 145))
        pygame.display.update()

    @staticmethod
    def draw_dashes(word):
        for i in range(len(word)):
            blank_line = pygame.image.load('Drawings/blank_line.png')
            window.blit(blank_line, (320 + (i*66) - ((66*(len(word)-1))/2), 619 + ((-1)**i)))
        pygame.display.update()

    @staticmethod
    def correct_guess(word, guess, letters, color=(0,0,0)):
        for occurance in range(len(word)):
            if word.find(guess, occurance) != -1:
                window.blit(letter_font.render(guess, True, color), (325 + (word.find(guess, occurance)*66) - ((66*(len(word)-1))/2), 555 + ((-1)**word.find(guess, occurance))))
        while guess in letters:
                letters.remove(guess)
        pygame.display.update()

    @staticmethod
    def wrong_guess(guess, wrong_guesses, color=(0,0,0)):
        if wrong_guesses == 1:
            head = pygame.image.load('Drawings/head.png')
            window.blit(head, (245, 192))
            window.blit(letter_font.render(guess, True, color), (424, 141))
        if wrong_guesses == 2:
            body = pygame.image.load('Drawings/body.png')
            window.blit(body, (275, 250))
            window.blit(letter_font.render(guess, True, color), (490, 141))
        if wrong_guesses == 3:
            left_arm = pygame.image.load('Drawings/left_arm.png')
            window.blit(left_arm, (237, 258))
            window.blit(letter_font.render(guess, True, color), (424, 221))
        if wrong_guesses == 4:
            right_arm = pygame.image.load('Drawings/right_arm.png')
            window.blit(right_arm, (282, 249))
            window.blit(letter_font.render(guess, True, color), (490, 221))
        if wrong_guesses == 5:
            left_leg = pygame.image.load('Drawings/left_leg.png')
            window.blit(left_leg, (250, 313))
            window.blit(letter_font.render(guess, True, color), (424, 301))
        if wrong_guesses == 6:
            right_leg = pygame.image.load('Drawings/right_leg.png')
            window.blit(right_leg, (282, 313))
            window.blit(letter_font.render(guess, True, color), (490, 301))
            dead = pygame.image.load('Drawings/dead.png')
            window.blit(dead, (260, 208))
        pygame.display.update()

    @staticmethod
    def previous_guess(guess, old_guesses, new_guess=True):
        for old_guess in old_guesses:
            if guess == old_guess:
                new_guess = False
        return new_guess

    @staticmethod
    def gameover(word, letters, wrong_guesses, game_over=False, red=(255,0,0), green=(50,205,50)):
        if wrong_guesses == 6:
            game_over = True
            window.blit(title_font.render('You Lose', True, red), (145, 432))
            for letter in letters:
                for occurance in range(len(word)):
                    if word.find(letter, occurance) != -1:
                        window.blit(letter_font.render(letter, True, red), (325 + (word.find(letter, occurance)*66) - ((66*(len(word)-1))/2), 555 + ((-1)**word.find(letter, occurance))))
        elif len(letters) == 0:
            game_over = True
            window.blit(title_font.render('You Win!', True, green), (145, 432))
            if wrong_guesses > 0:
                smile = pygame.image.load('Drawings/smile.png')
                window.blit(smile, (261, 210))
        pygame.display.update()
        return game_over

    @staticmethod
    def play_again():
        window.blit(small_font.render('Press any key to play again', True, (0,0,0)), (180, 720))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    return

    @staticmethod
    def key_press():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    guess = event.unicode
                    if guess.isalpha():
                        guess = guess.lower()
                        return guess
