# Hangman for Intel KTWD 2019
# by Michael Ruscito
import pygame, sys, random, time, tkinter as tk
from tkinter import messagebox

# random words
random_words = ['intel', 'computer', 'drive', 'power', 'memory', 'cpu', 'wonderful', 'genuis', 'keyboard', 'future', 'monitor', 'internet', 'gigabyte', 'data', 'program',
                'java', 'python', 'laptop', 'encrypt', 'flash', 'hacker', 'chip', 'code', 'icon', 'app', 'phone', 'tech', 'keyboard', 'mouse', 'speed', 'diode', 'logic',
                'electric', 'science', 'engineer', 'core', 'plug', 'charge', 'physics', 'fun', 'google', 'learn', 'email', 'screen', 'webcam', 'shock', 'voltage', 'current',
                'microsoft', 'apple', 'android', 'windows', 'linux', 'nanometer', 'processor', 'bluetooth', 'wifi', 'bits', 'robotics', 'code', 'wire', 'command', 'pentium',
                'tomorrow', 'battery', 'capacitor', 'induction', 'clock', 'binary', 'assembly', 'graphics', 'disk', 'smart', ]

'''
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
'''

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

'''
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
'''

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
'''
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
'''

def play_game():
    play_button.pack_forget()
    initialize_game()
    main_menu()
    draw_display()
    game_loop()
    time.sleep(2)
    root.lift()


# -----------------------------------------GUI Creation-----------------------------------------

# acceptable key words for each line of code
draw_key_words = ['draw', 'make', 'put', 'create', 'write', 'put', ]
line2_key_words = ['gallow', 'gallows', 'noose', 'rope', 'hangman', 'platform', 'hanging', 'block', 'upsidedown', 'game', 'board', 'gameboard', ]
line3_key_words = ['spaces', 'blanks', 'lines', 'letter', 'underscore', 'underscores', 'space', 'blank', 'line', ]
line5_key_words = ['guess', 'give', 'guesses', 'gives', ]
line6_key_words = ['correct', 'right', 'in', 'good', 'correctly', ]
line8_key_words = ['incorrect', 'wrong', 'not', 'bad', 'incorrectly', ]
line10_key_words = ['word', 'complete', 'letters', 'blanks', 'spaces', 'completed', ]
line11_key_words = ['win', 'won', 'victory', 'champion', 'wins', ]
line13_key_words = ['body', 'dead', 'person', 'hangman', 'hung', ]
line14_key_words = ['lose', 'loses', 'lost', 'loser', ]


# check that the word is properly defined
def test_line1():
    try:
        line1 = code_lines[0]
        global word
        global error_code
        line_broken = line1.split('=')
        word = line_broken[1]
        while not word[0].isalpha():
            word = word[1:]
        while not word[-1].isalpha():
            word = word[:-1]
        if word == 'random':
            word = random.choice(random_words)
        if len(word) > 9:
            code_box.tag_config('line1', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your first line of code.\nPlease enter a shorter word.\n9 character maximum.')
            error_code = 1
        elif not word.isalpha():
            code_box.tag_config('line1', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your first line of code.\nOnly letters are allowed.\nNo numbers, spaces, or special characters.')
            error_code = 1
        word = word.lower()
        global word_list
        word_list = list(word)
    except:
        code_box.tag_config('line1', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your first line of code.\nMake sure that you are defining your word properly.\nExample: word = "intel"')
        error_code = 1


def test_line2():
    try:
        line2 = code_lines[1].lower()
        global error_code
        error_code = 2
        line_broken = line2.split(' ')
        draw_key_word = line_broken[0]
        for key_word in line_broken[1:]:
            if key_word in line2_key_words or key_word in line3_key_words:
                key_word2 = key_word
        if draw_key_word in draw_key_words:
            if key_word2 in line2_key_words:
                error_code = 0
            elif key_word2 in line3_key_words:
                error_code = 0
        if line2[:15] == 'for each letter':
            error_code = 0
        if error_code == 2:
            code_box.tag_config('line2', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your second line of code.\nMake sure that you are drawing the game properly.\nExample: Draw gallows')
    except:
        code_box.tag_config('line2', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your second line of code.\nMake sure that you are drawing the game properly.\nExample: Draw gallows')
        error_code = 2


def test_line3():
    try:
        line3 = code_lines[2].lower()
        global error_code
        error_code = 3
        line_broken = line3.split(' ')
        draw_key_word = line_broken[0]
        for key_word in line_broken[1:]:
            if key_word in line2_key_words or key_word in line3_key_words:
                key_word3 = key_word
        if draw_key_word in draw_key_words:
            if key_word3 in line2_key_words:
                error_code = 0
            elif key_word3 in line3_key_words:
                error_code = 0
        if line3[:15] == 'for each letter':
            error_code = 0
        if error_code == 3:
            code_box.tag_config('line3', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your third line of code.\nMake sure that you are drawing the game properly.\nExample: Draw blanks')
    except:
        code_box.tag_config('line3', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your third line of code.\nMake sure that you are drawing the game properly.\nExample: Draw blanks')
        error_code = 3


def test_line4():
    try:
        line4 = code_lines[3].lower()
        global error_code
        error_code = 4
        line_broken = line4.split(' ')
        while_key_word = line_broken[0]
        if while_key_word == 'while':
            error_code = 0
        if error_code == 4:
            code_box.tag_config('line4', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your fourth line of code.\nDo not forget to create a loop that the game will repeat.\nExample: While the game is not over')
    except:
        code_box.tag_config('line4', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your fourth line of code.\nDo not forget to create a loop that the game will repeat.\nExample: While the game is not over')
        error_code = 4


def test_line5():
    try:
        line5 = code_lines[4].lower()
        global error_code
        error_code = 5
        line_broken = line5.split(' ')
        for key_word in line5_key_words:
            if key_word in line_broken:
                error_code = 0
        if error_code == 5:
            code_box.tag_config('line5', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your fifth line of code.\nMake sure that letters are being guessed for the game.\nExample: Player guesses a letter')
    except:
        code_box.tag_config('line5', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your fifth line of code.\nMake sure that letters are being guessed for the game.\nExample: Player guesses a letter')
        error_code = 5


def test_line7():
    try:
        global error_code
        if error_code == 6:
            line7 = code_lines[6].lower()
            error_code = 7
            line_broken = line7.split(' ')
            draw_key_word = line_broken[0]
            if draw_key_word in draw_key_words:
                error_code = 0
            if error_code == 7:
                code_box.tag_config('line7', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your seventh line of code.\nMake sure that correct guesses are written in the spaces.\nExample: Draw the letter in the blank')
        elif error_code == 8:
            line7 = code_lines[8].lower()
            error_code = 7
            line_broken = line7.split(' ')
            draw_key_word = line_broken[0]
            if draw_key_word in draw_key_words:
                error_code = 0
            if error_code == 7:
                code_box.tag_config('line9', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your ninth line of code.\nMake sure that correct guesses are written in the spaces.\nExample: Draw the letter in the blank')
    except:
        if error_code == 6:
            code_box.tag_config('line7', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your seventh line of code.\nMake sure that correct guesses are written in the spaces.\nExample: Draw the letter in the blank')
            error_code = 7
        if error_code == 8:
            code_box.tag_config('line9', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your ninth line of code.\nMake sure that correct guesses are written in the spaces.\nExample: Draw the letter in the blank')
            error_code = 7


def test_line9():
    try:
        global error_code
        if error_code == 6:
            line9 = code_lines[6].lower()
            error_code = 9
            line_broken = line9.split(' ')
            draw_key_word = line_broken[0]
            if draw_key_word in draw_key_words:
                error_code = 0
            if error_code == 9:
                code_box.tag_config('line7', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your seventh line of code.\nMake sure that body parts are drawn after incorrect guesses.\nExample: Draw a body part')
        elif error_code == 8:
            line9 = code_lines[8].lower()
            error_code = 9
            line_broken = line9.split(' ')
            draw_key_word = line_broken[0]
            if draw_key_word in draw_key_words:
                error_code = 0
            if error_code == 9:
                code_box.tag_config('line9', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your ninth line of code.\nMake sure that body parts are drawn after incorrect guesses.\nExample: Draw a body part')
    except:
        if error_code == 6:
            code_box.tag_config('line7', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your seventh line of code.\nMake sure that body parts are drawn after incorrect guesses.\nExample: Draw a body part')
            error_code = 9
        if error_code == 8:
            code_box.tag_config('line9', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your ninth line of code.\nMake sure that body parts are drawn after incorrect guesses.\nExample: Draw a body part')
            error_code = 9


def test_line6():
    try:
        line6 = code_lines[5].lower()
        global error_code
        error_code = 6
        line_broken = line6.split(' ')
        if_key_word = line_broken[0]
        test_pass = False
        if if_key_word == 'if':
            for key_word in line_broken[1:]:
                if key_word in line6_key_words:
                    correct = True
                if key_word in line8_key_words:
                    correct = False
            if correct:
                code_box.tag_config('line6', background='#7CFC00')
                test_pass = True
                test_line7()
            if not correct:
                code_box.tag_config('line6', background='#7CFC00')
                test_pass = True
                test_line9()
        if error_code == 6 and not test_pass:
            code_box.tag_config('line6', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your sixth line of code.\nMake sure that guesses are being checked by a conditional statement.\nExample: If the guess is correct')
    except:
        code_box.tag_config('line6', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your sixth line of code.\nMake sure that guesses are being checked by a conditional statement.\nExample: If the guess is correct')
        error_code = 6


def test_line8():
    try:
        line8 = code_lines[7].lower()
        global error_code
        error_code = 8
        line_broken = line8.split(' ')
        if_key_word = line_broken[0]
        test_pass = False
        if if_key_word == 'if' or if_key_word == 'else':
            for key_word in line_broken[1:]:
                if key_word in line6_key_words:
                    correct = True
                if key_word in line8_key_words:
                    correct = False
            if correct:
                code_box.tag_config('line8', background='#7CFC00')
                test_pass = True
                test_line7()
            if not correct:
                code_box.tag_config('line8', background='#7CFC00')
                test_pass = True
                test_line9()
        if error_code == 8 and not test_pass:
            code_box.tag_config('line8', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your eighth line of code.\nMake sure that guesses are being checked by a conditional statement.\nExample: If the guess is incorrect')
    except:
        code_box.tag_config('line8', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your eighth line of code.\nMake sure that guesses are being checked by a conditional statement.\nExample: If the guess is incorrect')
        error_code = 8


def test_line12():
    try:
        line12 = code_lines[11].lower()
        global error_code
        error_code = 12
        line_broken = line12.split(' ')
        for key_word in line_broken:
            if key_word in line11_key_words or key_word == 'game':
                error_code = 0
        if error_code == 12:
            code_box.tag_config('line12', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your twelfth line of code.\nDo not forget to close your while-loop.\nExample: The game is over')
    except:
        code_box.tag_config('line12', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your twelfth line of code.\nDo not forget to close your while-loop.\nExample: The game is over')
        error_code = 12


def test_line15():
    try:
        line15 = code_lines[14].lower()
        global error_code
        error_code = 15
        line_broken = line15.split(' ')
        for key_word in line_broken:
            if key_word in line14_key_words or key_word == 'game':
                error_code = 0
        if error_code == 15:
            code_box.tag_config('line15', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your fifteenth line of code.\nDo not forget to close your while-loop.\nExample: The game is over')
    except:
        code_box.tag_config('line15', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your fifteenth line of code.\nDo not forget to close your while-loop.\nExample: The game is over')
        error_code = 15


def test_line11():
    try:
        global error_code
        test_pass = False
        if error_code == 10:
            line11 = code_lines[10].lower()
            error_code = 11
            line_broken = line11.split(' ')
            for key_word in line_broken:
                if key_word in line11_key_words:
                    code_box.tag_config('line11', background='#7CFC00')
                    test_pass = True
                    test_line12()
                elif key_word == 'game':
                    code_box.tag_config('line11', background='#7CFC00')
                    test_pass = True
                    test_line12()
            if error_code == 11 and not test_pass:
                code_box.tag_config('line11', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your eleventh line of code.\nDo not forget to declare the winner.\nExample: Player wins the game!')
        elif error_code == 13:
            line11 = code_lines[13].lower()
            error_code = 11
            line_broken = line11.split(' ')
            for key_word in line_broken:
                if key_word in line11_key_words:
                    code_box.tag_config('line14', background='#7CFC00')
                    test_pass = True
                    test_line15()
                elif key_word == 'game':
                    code_box.tag_config('line14', background='#7CFC00')
                    test_pass = True
                    test_line15()
            if error_code == 13 and not test_pass:
                code_box.tag_config('line11', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your fourteenth line of code.\nDo not forget to declare the winner.\nExample: Player wins the game!')
    except:
        if error_code == 10:
            code_box.tag_config('line11', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your eleventh line of code.\nDo not forget to declare the winner.\nExample: Player wins the game!')
            error_code = 11
        if error_code == 13:
            code_box.tag_config('line14', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your fourteenth line of code.\nDo not forget to declare the winner.\nExample: Player wins the game!')
            error_code = 11


def test_line14():
    try:
        global error_code
        test_pass = False
        if error_code == 10:
            line14 = code_lines[10].lower()
            error_code = 14
            line_broken = line14.split(' ')
            for key_word in line_broken:
                if key_word in line14_key_words:
                    code_box.tag_config('line11', background='#7CFC00')
                    test_pass = True
                    test_line12()
                elif key_word == 'game':
                    code_box.tag_config('line11', background='#7CFC00')
                    test_pass = True
                    test_line12()
            if error_code == 14 and not test_pass:
                code_box.tag_config('line11', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your eleventh line of code.\nDo not forget to declare a loser.\nExample: Player loses the game')
        elif error_code == 13:
            line14 = code_lines[13].lower()
            error_code = 14
            line_broken = line14.split(' ')
            for key_word in line_broken:
                if key_word in line11_key_words:
                    code_box.tag_config('line14', background='#7CFC00')
                    test_pass = True
                    test_line15()
                elif key_word == 'game':
                    code_box.tag_config('line14', background='#7CFC00')
                    test_pass = True
                    test_line15()
            if error_code == 14 and not test_pass:
                code_box.tag_config('line14', background='red')
                messagebox.showerror('Error', 'There appears to be an error with your fourteenth line of code.\nDo not forget to declare a loser.\nExample: Player loses the game')
    except:
        if error_code == 10:
            code_box.tag_config('line14', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your eleventh line of code.\nDo not forget to declare a loser.\nExample: Player loses the game')
            error_code = 14
        if error_code == 13:
            code_box.tag_config('line14', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your fourteenth line of code.\nDo not forget to declare a loser.\nExample: Player loses the game')
            error_code = 14


def test_line10():
    try:
        line10 = code_lines[9].lower()
        global error_code
        error_code = 10
        line_broken = line10.split(' ')
        if_key_word = line_broken[0]
        test_pass = False
        if if_key_word == 'if':
            for key_word in line_broken[1:]:
                if key_word in line10_key_words:
                    victory = True
                if key_word in line13_key_words:
                    victory = False
            if victory:
                code_box.tag_config('line10', background='#7CFC00')
                test_pass = True
                test_line11()
            if not victory:
                code_box.tag_config('line10', background='#7CFC00')
                test_pass = True
                test_line14()
        if error_code == 10 and not test_pass:
            code_box.tag_config('line10', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your tenth line of code.\nDo not forget a conditional statement to check if the game is over.\nExample: If the word is complete')
    except:
        code_box.tag_config('line10', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your tenth line of code.\nDo not forget a conditional statement to check if the game is over.\nExample: If the word is complete')
        error_code = 10


def test_line13():
    try:
        line13 = code_lines[12].lower()
        global error_code
        error_code = 13
        line_broken = line13.split(' ')
        if_key_word = line_broken[0]
        test_pass = False
        if if_key_word == 'if':
            for key_word in line_broken[1:]:
                if key_word in line10_key_words:
                    victory = True
                if key_word in line13_key_words:
                    victory = False
            if victory:
                code_box.tag_config('line13', background='#7CFC00')
                test_pass = True
                test_line11()
            if not victory:
                code_box.tag_config('line13', background='#7CFC00')
                test_pass = True
                test_line14()
        if error_code == 13 and not test_pass:
            code_box.tag_config('line13', background='red')
            messagebox.showerror('Error', 'There appears to be an error with your thirteenth line of code.\nDo not forget a conditional statement to check if the game is over.\nExample: If the body is fully drawn')
    except:
        code_box.tag_config('line13', background='red')
        messagebox.showerror('Error', 'There appears to be an error with your thirteenth line of code.\nDo not forget a conditional statement to check if the game is over.\nExample: If the body is fully drawn')
        error_code = 13


def check_code_length():
    try:
        line17 = code_lines[16]
        global error_code
        if len(line17) > 0:
            error_code = 17
            code_box.tag_config('line16', background='red')
            messagebox.showerror('Error', 'There appears to be an error with the length of your of code.\nYour code is too long. Try shortening it.')
    except:
        pass


def test_code():
    code_box.tag_add('line1', '1.0', '1.80')
    code_box.tag_add('line2', '2.0', '2.80')
    code_box.tag_add('line3', '3.0', '3.80')
    code_box.tag_add('line4', '4.0', '4.80')
    code_box.tag_add('line5', '5.0', '5.80')
    code_box.tag_add('line6', '6.0', '6.80')
    code_box.tag_add('line7', '7.0', '7.80')
    code_box.tag_add('line8', '8.0', '8.80')
    code_box.tag_add('line9', '9.0', '9.80')
    code_box.tag_add('line10', '10.0', '10.80')
    code_box.tag_add('line11', '11.0', '11.80')
    code_box.tag_add('line12', '12.0', '12.80')
    code_box.tag_add('line13', '13.0', '13.80')
    code_box.tag_add('line14', '14.0', '14.80')
    code_box.tag_add('line15', '15.0', '15.80')
    code_box.tag_add('line16', '16.0', '16.80')
    code_box.tag_config('line1', background='white')
    code_box.tag_config('line2', background='white')
    code_box.tag_config('line3', background='white')
    code_box.tag_config('line4', background='white')
    code_box.tag_config('line5', background='white')
    code_box.tag_config('line6', background='white')
    code_box.tag_config('line7', background='white')
    code_box.tag_config('line8', background='white')
    code_box.tag_config('line9', background='white')
    code_box.tag_config('line10', background='white')
    code_box.tag_config('line11', background='white')
    code_box.tag_config('line12', background='white')
    code_box.tag_config('line13', background='white')
    code_box.tag_config('line14', background='white')
    code_box.tag_config('line15', background='white')
    code_box.tag_config('line16', background='white')
    play_button.pack_forget()
    global word
    word = ''
    global error_code
    error_code = 0
    global code_lines
    code_lines = code_box.get('0.0', 'end').split('\n')
    code_lines.pop()
    for line in code_lines:
        # get rid of tabs
        if '\t' in line:
            fixed_line = ''
            line_list = line.split('\t')
            for word in line_list:
                fixed_line += word
            code_lines[code_lines.index(line)] = fixed_line
    # test each line of code
    test_line1()
    if error_code == 0:
        code_box.tag_config('line1', background='#7CFC00')
        test_line2()
        if error_code == 0:
            code_box.tag_config('line2', background='#7CFC00')
            test_line3()
            if error_code == 0:
                code_box.tag_config('line3', background='#7CFC00')
                test_line4()
                if error_code == 0:
                    code_box.tag_config('line4', background='#7CFC00')
                    test_line5()
                    if error_code == 0:
                        code_box.tag_config('line5', background='#7CFC00')
                        test_line6()
                        if error_code == 0:
                            code_box.tag_config('line7', background='#7CFC00')
                            test_line8()
                            if error_code == 0:
                                code_box.tag_config('line9', background='#7CFC00')
                                test_line10()
                                if error_code == 0:
                                    code_box.tag_config('line12', background='#7CFC00')
                                    test_line13()
                                    if error_code == 0:
                                        code_box.tag_config('line15', background='#7CFC00')
                                        code_box.tag_config('line16', background='#7CFC00')
                                        check_code_length()
                                        if error_code == 0:
                                            play_button.pack()
    


def pseudo_code():
    global root
    root = tk.Tk()
    root.title('Intel KTWD Hangman')
    #root.configure(bg='black')
    code_label = tk.Label(root, text='Enter your code here:')
    code_label.pack()
    global code_box
    code_box = tk.Text(root) #, bg='black', fg='white', insertbackground='white')
    code_box.pack()
    test_button = tk.Button(root, text='Test My Code', command=test_code)
    test_button.pack()
    global play_button
    play_button = tk.Button(root, text='Play Hangman!', command=play_game)
    root.mainloop()
    

pseudo_code()
