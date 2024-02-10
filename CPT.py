#import pygame
import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
YELLOW   = ( 244, 252,   3)
AQUA     = ( 111, 202, 232)
BRICK    = ( 212, 144, 156)
DGREEN   = (  73, 107,  51)
DPINK    = ( 255,   0, 102)
LBLUE    = (   0, 153, 255)
ORANGE   = ( 255, 153,   0)

#backed grid for game
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print (grid)

pygame.init()
# Set the width and height of the screen
size = (700, 650)
screen = pygame.display.set_mode(size)
#name on title bar
pygame.display.set_caption("TicTacToe!")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#this function draws the restart button
def drawRestartButton():
    pygame.draw.rect(screen,BRICK,[195,566,100,33])
    restartFont = pygame.font.SysFont('Serif', 15, True, False)
    title = restartFont.render("Restart",True,DGREEN)
    screen.blit(title, [220, 575])

#this function draws the exit button
def drawExitButton(x1,y1,x2,y2):
    pygame.draw.rect(screen,BRICK,[x1,y1,100,33])
    restartFont = pygame.font.SysFont('Serif', 15, True, False)
    title = restartFont.render("Exit",True,DGREEN)
    screen.blit(title, [x2, y2])

#fonts
gameoverfont = pygame.font.SysFont('Arial', 15, True, False)
game_over = gameoverfont.render("Game Over! ",True,BLACK)
finish_font = pygame.font.SysFont('Arial', 15, True, False)

#this function is used to display the outcome of a game
def drawWinnerMessage(win):
    if win == 1:
        screen.blit(finish_font.render("X Wins! ",True,BLACK), [318, 535])
    elif win == 2:
        screen.blit(finish_font.render("O Wins! ",True,BLACK), [318, 535])
    elif win == 17:
        screen.blit(finish_font.render("Draw! ",True,BLACK), [318, 535])

#this function draws the details depending on game mode
def drawGamePageDetails(x):
    gameoverfont = pygame.font.SysFont('Arial', 15, True, False)
    game_over = gameoverfont.render("Game Over! ",True,BLACK)
    if x == 1:
        screen.fill(AQUA)
        screen.blit(title_multiplayer, [141,50])
    elif x == 2:
        screen.fill(ORANGE)
        screen.blit(title_singleplayer, [141,50])
    title_font = pygame.font.SysFont('Calibri', 25, True, False)
    other_font = pygame.font.SysFont('Arial', 15, True, False)
    title = title_font.render("Welcome to Tic Tac Toe!",True,BLACK)
    credit_display = other_font.render("Made by Christian D'Souza ",True,BLACK)
    screen.blit(title, [215, 150])
    screen.blit(credit_display, [ 525, 625])

#set up variables to determine turns for players
player_X = 0
player_O = 0
turn = 1

#this variable is used to end the game once a winner is determined;
won_game = 0
winner_param = [-1,-1,-1,-1,0] #stores the winning line parameters and game outcome

#this function states the winnner and the winning line from (x1,y1) to (x2,y2)
def drawDetermineWinner(x1, y1, x2, y2, winner):
    if winner != 0: #if the game is completed
        screen.blit(game_over, [318, 515])
        drawWinnerMessage(winner)
        pygame.draw.line(screen, RED, [x1, y1], [x2, y2], 4)

#this function has all the home screen buttons drawn
def drawMultiplayerButton():
    pygame.draw.rect(screen,WHITE,[25,300,150,50],0)
    pygame.draw.rect(screen,DPINK,[25,300,150,50], 2)
    pygame.draw.rect(screen,WHITE,[525,300,150,50],0)
    pygame.draw.rect(screen,DPINK,[525,300,150,50], 2)
    pygame.draw.rect(screen,WHITE,[275,400,150,50],0)
    pygame.draw.rect(screen,DPINK,[275,400,150,50], 2)
    menufont = pygame.font.SysFont('Arial', 25, True, False)
    singleplayer = gameoverfont.render("Singleplayer ",True,DPINK)
    multiplayer = gameoverfont.render("Multiplayer ",True,DPINK)
    how_to_play = gameoverfont.render("How To Play",True,DPINK)
    screen.blit(singleplayer, [60, 315])
    screen.blit(multiplayer, [565, 315])
    screen.blit(how_to_play, [315, 415])

#this function checks if a win exists in the game, and modifies the winning parameter
def checkIfWin():
    '''winning conditions for both players'''
    for i in range(0,3):
        #vertical win
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i] != 0:
            return [1, [245+i*103, 195, 245+i*103, 501, grid[0][i]]]
        #horizontal win
        elif grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][0] != 0:
            return [1, [195, 245+i*103, 501, 245+i*103, grid[i][0]]]
    #diagonal win top right to bottom left
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != 0:
        return [1, [195, 501, 501, 195, grid[0][2]]]
    #diagonal win top left to bottom right
    elif grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != 0:
        return [1, [195, 195, 501, 501, grid[0][0]]]
    for x in range(0,3): #check if tie or game still going on
        if grid[0][x] == 0 or grid[1][x] == 0 or grid[2][x] == 0:
            return [0,[-1,-1,-1,-1,0]]
    return [17,[-1,-1,-1,-1,17]]

#this function designs the screen based on the game mode
def game_screen(type,win,param):
    drawGamePageDetails(type)
    drawRestartButton()
    drawExitButton(401,566,436,575)
    for i in range(3): #draws empty board
        for x in range(3):
            pygame.draw.rect(screen,WHITE,[195+(103*i),195+(103*x),100,100])
    for i in range(0,3):
        for x in range(0,3):
            if grid[i][x] == 1: #draws an X
                pygame.draw.rect(screen,GREEN,[(225+103*x)-30,(225+103*i)-30,100,100])
                pygame.draw.line(screen, BLACK, [225+103*x, 225+103*i], [(225+103*x)+40, (225+103*i)+40], 3)
                pygame.draw.line(screen, BLACK, [(225+103*x)+40, 225+103*i], [(225+103*x), (225+103*i)+40], 3)
            elif grid[i][x] == 2: #draws an O
                pygame.draw.rect(screen,YELLOW,[(225+103*x)-30,(225+103*i)-30,100,100])
                pygame.draw.ellipse(screen, BLACK, [225+103*x,225+103*i,40,40],3)
    #check if game is already over
    if win == 1 or win == 17: #checks if the game is already over by win
        drawDetermineWinner(param[0],param[1],param[2],param[3],param[4])
        return [win,param]
    #now check if the game is over or still going
    checkResult = checkIfWin()
    return [checkResult[0],checkResult[1]]

#loading all images
example_image = pygame.image.load("howtoplayexample.jpg").convert()
homescreen_image = pygame.image.load("homepagetitle.jpg").convert()
background_image_homescreen = pygame.image.load("cptbackground_1.jpg").convert()
how_to_play = pygame.image.load("cpt_how_to_play_background.jpg")
how_to_play_title = pygame.image.load("title_how_to_play.jpg").convert()
how_to_play_instructions = pygame.image.load("instructions_how_to_play.jpg").convert()
title_multiplayer = pygame.image.load("multi_player_title.jpg").convert()
title_singleplayer = pygame.image.load("single_player_title.jpg").convert()

#setting home_screen = 0, so it automatically starts with the home screen
home_screen = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
# --- Game logic should go here
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            posx = position[0]
            posy = position[1]
            if home_screen == 0: #home screen
                if posy >= 300 and posy <= 350:
                    if posx >= 525 and posx <= 675:
                        home_screen = 1
                    elif posx >= 25 and posx <= 175:
                        home_screen = 2
                if posy >= 400 and posy <= 450:
                    if posx >= 275 and posx <= 425:
                        home_screen = 3
            elif home_screen == 3: #how to play screen
                if posy >= 601 and posy <= 634:
                    if posx >= 580 and posx <= 680:
                        home_screen = 0
            elif home_screen == 1 or home_screen == 2: #game screen (multiplayer and singleplayer)
                for x in range(0,3): #store choice on board depending on where user clicks
                    if posx >= 195+x*103 and posx <= 295+x*103:
                        for i in range(0,3):
                            if posy >= 195+i*103 and posy <= 295+i*103:
                                if grid[i][x] == 0 and won_game == 0:
                                    grid[i][x] = turn
                                    print (grid)
                                    if turn == 1:
                                        turn += 1
                                    else:
                                        turn -= 1
                                    break
                            elif posy >= 566 and posy <= 599 and x != 1:
                                grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                                turn = 1
                                won_game = 0
                                if x == 2:
                                    home_screen = 0
                                break
                if home_screen == 2 and turn == 2: #these conditions are for singleplayer bot strategies
                    #if X starts anywhere but the middle, O plays the middle
                    if grid == [[1, 0, 0], [0, 0, 0], [0, 0, 0]] or grid == [[0, 0, 1], [0, 0, 0], [0, 0, 0]] or grid == [[0, 0, 0], [0, 0, 0], [1, 0, 0]] or grid == [[0, 0, 0], [0, 0, 0], [0, 0, 1]] or grid == [[0, 1, 0], [0, 0, 0], [0, 0, 0]] or grid == [[0, 0, 0], [1, 0, 0], [0, 0, 0]] or grid == [[0, 0, 0], [0, 0, 1], [0, 0, 0]] or grid == [[0, 0, 0], [0, 0, 0], [0, 1, 0]]:
                        grid[1][1] = 2
                    #if X starts in the middle, O plays top-left corner
                    elif grid == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]:
                        grid[0][0] = 2
                    #second move
                    elif grid == [[1, 0, 0], [1, 2, 0], [0, 0, 0]] or grid == [[2, 0, 1], [0, 1, 0], [0, 0, 0]] or grid == [[2, 0, 0], [0, 1, 0], [0, 0, 1]] or grid == [[1, 0, 0], [0, 2, 0], [0, 1, 0]] or grid == [[0, 0, 0], [0, 2, 0], [0, 1, 1]] or grid == [[0, 0, 0], [1, 2, 0], [0, 1, 0]]:
                        grid[2][0] = 2
                    elif grid == [[1, 0, 0], [0, 2, 0], [1, 0, 0]] or grid == [[2, 0, 0], [0, 1, 1], [0, 0, 0]] or grid == [[0, 1, 0], [0, 2, 0], [1, 0, 0]]:
                        grid[1][0] = 2
                    elif grid == [[1, 0, 0], [0, 2, 0], [0, 0, 1]] or grid == [[2, 1, 0], [0, 1, 0], [0, 0, 0]] or grid == [[0, 0, 0], [0, 2, 0], [1, 0, 1]]:
                        grid[2][1] = 2
                    elif grid == [[1, 0, 0], [0, 2, 1], [0, 0, 0]] or grid == [[2, 0, 0], [0, 1, 0], [0, 1, 0]] or grid == [[0, 0, 0], [1, 2, 0], [0, 0, 1]] or grid == [[1, 0, 1], [0, 2, 0], [0, 0, 0]] or grid == [[0, 0, 1], [1, 2, 0], [0, 0, 0]] or grid == [[0, 0, 1], [0, 2, 0], [1, 0, 0]] or grid == [[0, 0, 0], [0, 2, 1], [1, 0, 0]]:
                        grid[0][1] = 2
                    elif grid == [[1, 1, 0], [0, 2, 0], [0, 0, 0]] or grid == [[2, 0, 0], [0, 1, 0], [1, 0, 0]] or grid == [[0, 1, 0], [0, 2, 0], [0, 1, 0]] or grid == [[0, 1, 0], [0, 2, 0], [0, 0, 1]] or grid == [[0, 1, 0], [0, 2, 1], [0, 0, 0]] or grid == [[0, 0, 0], [0, 2, 1], [0, 0, 1]]:
                        grid[0][2] = 2
                    elif grid == [[0, 1, 0], [1, 2, 0], [0, 0, 0]] or grid == [[0, 1, 1], [0, 2, 0], [0, 0, 0]] or grid == [[0, 0, 0], [1, 2, 1], [0, 0, 0]] or grid == [[0, 0, 0], [1, 2, 0], [1, 0, 0]]:
                        grid[0][0] = 2
                    elif grid == [[0, 0, 1], [0, 2, 0], [0, 1, 0]] or grid == [[2, 0, 0], [1, 1, 0], [0, 0, 0]] or grid == [[0, 0, 1], [0, 2, 0], [0, 0, 1]]:
                        grid[1][2] = 2
                    elif grid == [[0, 0, 1], [0, 2, 1], [0, 0, 0]] or grid == [[0, 0, 0], [0, 2, 1], [0, 1, 0]] or grid == [[0, 0, 0], [0, 2, 0], [1, 1, 0]]:
                        grid[2][2] = 2
                    #third move
                    elif grid == [[1, 1, 2], [0, 2, 0], [1, 0, 0]] or grid == [[2, 0, 0], [0, 1, 0], [2, 1, 1]] or grid == [[2, 0, 0], [0, 1, 1], [2, 0, 1]] or grid == [[2, 1, 0], [0, 1, 0], [2, 0, 1]] or grid == [[2, 0, 1], [0, 1, 0], [2, 0, 1]] or grid == [[2, 0, 1], [0, 1, 0], [2, 1, 0]] or grid == [[2, 0, 1], [0, 1, 1], [2, 0, 0]] or grid == [[2, 1, 1], [0, 1, 0], [2, 0, 0]] or grid == [[2, 1, 0], [0, 1, 0], [0, 2, 1]] or grid == [[2, 1, 0], [0, 1, 1], [0, 2, 0]] or grid == [[1, 0, 0], [0, 2, 0], [1, 1, 2]] or grid == [[0, 1, 0], [0, 2, 0], [1, 2, 1]] or grid == [[0, 1, 1], [0, 2, 2], [0, 1, 0]] or grid == [[1, 0, 1], [0, 2, 2], [0, 1, 0]] or grid == [[0, 0, 1], [0, 2, 2], [1, 1, 0]] or grid == [[1, 0, 1], [0, 2, 2], [0, 0, 1]] or grid == [[0, 1, 1], [0, 2, 2], [0, 0, 1]] or grid == [[0, 0, 1], [0, 2, 2], [1, 0, 1]] or grid == [[0, 0, 1], [0, 2, 2], [0, 1, 1]]:
                        grid[1][0] = 2
                    elif grid == [[1, 1, 2], [1, 2, 0], [0, 0, 0]] or grid == [[2, 0, 1], [1, 1, 2], [0, 0, 0]] or grid == [[2, 2, 1], [0, 1, 0], [0, 1, 0]] or grid == [[2, 0, 0], [2, 1, 1], [0, 0, 1]] or grid == [[2, 0, 0], [2, 1, 1], [0, 1, 0]] or grid == [[2, 0, 1], [2, 1, 1], [0, 0, 0]] or grid == [[2, 1, 0], [2, 1, 1], [0, 0, 0]] or grid == [[2, 1, 1], [0, 1, 0], [0, 2, 0]] or grid == [[0, 2, 0], [1, 2, 0], [0, 1, 1]] or grid == [[0, 0, 2], [0, 2, 1], [0, 1, 1]] or grid == [[0, 0, 2], [1, 2, 1], [0, 0, 1]] or grid == [[1, 0, 2], [0, 2, 1], [0, 0, 1]] or grid == [[0, 1, 2], [1, 2, 0], [0, 0, 1]] or grid == [[2, 1, 0], [1, 2, 0], [0, 0, 1]] or grid == [[0, 1, 2], [1, 2, 0], [0, 1, 0]] or grid == [[0, 1, 2], [0, 2, 0], [0, 1, 1]] or grid == [[0, 1, 2], [1, 2, 1], [0, 0, 0]] or grid == [[0, 1, 2], [0, 2, 1], [0, 1, 0]] or grid == [[0, 1, 2], [0, 2, 1], [0, 0, 1]] or grid == [[1, 2, 0], [0, 2, 1], [0, 1, 0]] or grid == [[1, 1, 2], [1, 2, 0], [0, 0, 0]] or grid == [[1, 1, 2], [0, 2, 1], [0, 0, 0]] or grid == [[1, 1, 2], [0, 2, 0], [0, 1, 0]] or grid == [[1, 1, 2], [0, 2, 0], [0, 0, 1]]:
                        grid[2][0] = 2
                    elif grid == [[1, 2, 1], [0, 2, 0], [0, 1, 0]] or grid == [[2, 0, 0], [1, 1, 0], [2, 0, 1]] or grid == [[2, 0, 1], [1, 1, 0], [2, 0, 0]] or grid == [[2, 1, 0], [1, 1, 0], [0, 2, 0]] or grid == [[0, 0, 1], [0, 2, 0], [2, 1, 1]] or grid == [[0, 1, 1], [2, 2, 0], [1, 0, 0]] or grid == [[0, 1, 0], [2, 2, 0], [1, 1, 0]] or grid == [[0, 1, 0], [2, 2, 0], [1, 0, 1]] or grid == [[2, 1, 1], [0, 2, 0], [0, 0, 1]] or grid == [[1, 1, 0], [2, 2, 0], [1, 0, 0]] or grid == [[1, 0, 0], [2, 2, 0], [1, 1, 0]] or grid == [[1, 0, 0], [2, 2, 0], [1, 0, 1]] or grid == [[1, 0, 1], [2, 2, 0], [1, 0, 0]]:
                        grid[1][2] = 2
                    elif grid == [[1, 2, 0], [0, 2, 1], [1, 0, 0]] or grid == [[2, 1, 0], [1, 1, 2], [0, 0, 0]] or grid == [[2, 1, 2], [0, 1, 0], [1, 0, 0]] or grid == [[2, 0, 0], [1, 2, 0], [1, 0, 1]] or grid == [[1, 2, 0], [1, 2, 0], [0, 0, 1]] or grid == [[0, 2, 0], [1, 2, 1], [0, 0, 1]] or grid == [[0, 2, 0], [1, 2, 0], [1, 0, 1]] or grid == [[0, 0, 2], [0, 2, 1], [1, 0, 1]] or grid == [[0, 2, 0], [1, 2, 1], [1, 0, 0]] or grid == [[0, 2, 0], [0, 2, 1], [1, 0, 1]] or grid == [[0, 2, 1], [1, 2, 1], [0, 0, 0]] or grid == [[0, 2, 1], [1, 2, 0], [0, 0, 1]] or grid == [[0, 2, 1], [1, 2, 0], [1, 0, 0]] or grid == [[0, 2, 1], [0, 2, 1], [1, 0, 0]] or grid == [[0, 2, 1], [0, 2, 0], [1, 0, 1]] or grid == [[0, 0, 1], [1, 2, 2], [0, 0, 1]] or grid == [[0, 1, 2], [0, 2, 0], [1, 0, 1]] or grid == [[1, 2, 0], [0, 2, 1], [0, 0, 1]] or grid == [[1, 2, 1], [1, 2, 0], [0, 0, 0]] or grid == [[1, 0, 0], [2, 2, 1], [1, 0, 0]] or grid == [[1, 2, 1], [0, 2, 1], [0, 0, 0]] or grid == [[1, 2, 1], [0, 2, 0], [1, 0, 0]] or grid == [[1, 2, 1], [0, 2, 0], [0, 0, 1]] or grid == [[1, 2, 0], [1, 2, 1], [0, 0, 0]]:
                        grid[2][1] = 2
                    elif grid == [[1, 1, 0], [1, 2, 0], [2, 0, 0]] or grid == [[2, 0, 0], [1, 1, 2], [0, 0, 1]] or grid == [[2, 0, 0], [1, 1, 2], [1, 0, 0]] or grid == [[2, 2, 0], [0, 1, 0], [0, 1, 1]] or grid == [[2, 2, 0], [0, 1, 0], [1, 1, 0]] or grid == [[2, 2, 0], [0, 1, 1], [0, 1, 0]] or grid == [[2, 2, 0], [1, 1, 0], [0, 1, 0]] or grid == [[2, 0, 0], [2, 1, 1], [1, 0, 0]] or grid == [[2, 1, 0], [0, 1, 0], [1, 2, 0]] or grid == [[0, 1, 0], [1, 2, 0], [2, 1, 0]] or grid == [[0, 0, 0], [1, 2, 1], [2, 1, 0]] or grid == [[0, 1, 0], [0, 2, 0], [2, 1, 1]] or grid == [[0, 0, 0], [1, 2, 0], [2, 1, 1]] or grid == [[0, 0, 0], [0, 2, 1], [2, 1, 1]] or grid == [[1, 0, 0], [0, 2, 1], [0, 1, 2]] or grid == [[2, 0, 0], [1, 2, 1], [0, 0, 1]] or grid == [[1, 0, 0], [1, 2, 1], [2, 0, 0]] or grid == [[1, 0, 0], [1, 2, 0], [2, 0, 1]] or grid == [[1, 1, 0], [0, 2, 0], [0, 2, 1]] or grid == [[1, 0, 0], [1, 2, 0], [2, 1, 0]] or grid == [[1, 1, 0], [0, 2, 0], [2, 1, 0]] or grid == [[1, 0, 0], [0, 2, 0], [2, 1, 1]] or grid == [[1, 0, 0], [0, 2, 1], [2, 1, 0]]:
                        grid[0][2] = 2
                    elif grid == [[1, 0, 1], [1, 2, 0], [2, 0, 0]] or grid == [[2, 0, 0], [1, 1, 2], [0, 1, 0]] or grid == [[2, 0, 2], [0, 1, 0], [1, 0, 1]] or grid == [[2, 0, 2], [0, 1, 0], [1, 1, 0]] or grid == [[2, 0, 2], [0, 1, 1], [1, 0, 0]] or grid == [[2, 0, 2], [1, 1, 0], [1, 0, 0]] or grid == [[0, 0, 1], [0, 2, 0], [1, 2, 1]] or grid == [[0, 0, 0], [1, 2, 0], [1, 2, 1]] or grid == [[0, 0, 0], [0, 2, 1], [1, 2, 1]] or grid == [[1, 0, 1], [0, 2, 1], [0, 0, 2]] or grid == [[1, 0, 1], [0, 2, 0], [2, 1, 0]] or grid == [[1, 0, 0], [1, 2, 0], [0, 2, 1]] or grid == [[1, 0, 0], [0, 2, 0], [1, 2, 1]] or grid == [[1, 0, 0], [0, 2, 1], [0, 2, 1]] or grid == [[1, 0, 1], [0, 2, 0], [0, 2, 1]]:
                        grid[0][1] = 2
                    elif grid == [[2, 1, 1], [1, 2, 0], [0, 0, 0]] or grid == [[0, 1, 2], [0, 2, 0], [1, 1, 0]] or grid == [[2, 0, 1], [1, 2, 0], [1, 0, 0]] or grid == [[2, 0, 0], [1, 2, 0], [1, 1, 0]] or grid == [[0, 2, 0], [0, 2, 1], [1, 1, 0]] or grid == [[2, 0, 1], [1, 2, 1], [0, 0, 0]] or grid == [[2, 0, 0], [1, 2, 1], [1, 0, 0]] or grid == [[2, 0, 0], [1, 2, 1], [0, 1, 0]] or grid == [[0, 2, 1], [1, 2, 0], [0, 1, 0]] or grid == [[0, 2, 1], [0, 2, 0], [1, 1, 0]] or grid == [[0, 1, 0], [2, 2, 1], [1, 0, 0]] or grid == [[2, 1, 0], [1, 2, 1], [0, 0, 0]] or grid == [[2, 1, 0], [1, 2, 0], [1, 0, 0]] or grid == [[2, 1, 0], [1, 2, 0], [0, 1, 0]] or grid == [[0, 1, 2], [0, 2, 1], [1, 0, 0]] or grid == [[2, 1, 1], [0, 2, 1], [0, 0, 0]] or grid == [[2, 1, 1], [0, 2, 0], [1, 0, 0]] or grid == [[2, 1, 1], [0, 2, 0], [0, 1, 0]]:
                        grid[2][2] = 2
                    elif grid == [[0, 1, 1], [0, 2, 1], [0, 0, 2]] or grid == [[0, 0, 0], [1, 2, 0], [1, 1, 2]] or grid == [[0, 1, 0], [0, 2, 0], [1, 1, 2]] or grid == [[0, 0, 1], [0, 2, 0], [1, 1, 2]] or grid == [[0, 0, 1], [1, 2, 0], [2, 1, 0]] or grid == [[0, 1, 0], [0, 2, 1], [0, 1, 2]] or grid == [[0, 0, 0], [1, 2, 1], [0, 1, 2]] or grid == [[0, 0, 0], [0, 2, 1], [1, 1, 2]] or grid == [[0, 0, 1], [1, 2, 2], [0, 1, 0]] or grid == [[0, 0, 1], [0, 2, 1], [0, 1, 2]] or grid == [[0, 0, 1], [1, 2, 1], [0, 0, 2]] or grid == [[0, 0, 1], [0, 2, 1], [1, 0, 2]]:
                        grid[0][0] = 2
                    #fourth move
                    elif grid == [[1, 1, 2], [2, 2, 0], [1, 1, 0]] or grid == [[2, 2, 1], [1, 1, 0], [2, 1, 0]] or grid == [[2, 1, 2], [1, 1, 0], [1, 2, 0]] or grid == [[2, 1, 0], [1, 2, 0], [1, 2, 1]] or grid == [[2, 0, 1], [1, 2, 0], [2, 1, 1]] or grid == [[1, 1, 0], [2, 2, 0], [1, 1, 2]] or grid == [[1, 0, 1], [2, 2, 0], [1, 1, 2]] or grid == [[0, 2, 1], [1, 2, 0], [2, 1, 1]] or grid == [[1, 1, 0], [2, 2, 0], [1, 2, 1]] or grid == [[0, 1, 1], [2, 2, 0], [1, 2, 1]] or grid == [[2, 1, 1], [1, 2, 0], [2, 0, 1]] or grid == [[1, 1, 2], [0, 2, 0], [1, 1, 2]] or grid == [[0, 1, 2], [1, 2, 0], [1, 1, 2]] or grid == [[1, 2, 1], [0, 2, 0], [2, 1, 1]] or grid == [[1, 2, 1], [1, 2, 0], [2, 1, 0]] or grid == [[1, 1, 2], [2, 2, 0], [1, 0, 1]]:
                        grid[1][2] = 2
                    elif grid == [[1, 1, 2], [2, 2, 1], [1, 0, 0]] or grid == [[2, 1, 2], [1, 1, 2], [0, 0, 1]] or grid == [[2, 1, 0], [1, 1, 2], [2, 0, 1]] or grid == [[2, 1, 2], [2, 1, 1], [1, 0, 0]] or grid == [[2, 1, 1], [1, 1, 2], [2, 0, 0]] or grid == [[1, 2, 1], [1, 2, 1], [0, 0, 2]] or grid == [[1, 2, 1], [0, 2, 1], [1, 0, 2]] or grid == [[1, 2, 1], [1, 2, 1], [2, 0, 0]] or grid == [[1, 2, 1], [1, 2, 0], [2, 0, 1]]:
                        grid[2][1] = 2
                    elif grid == [[1, 2, 1], [0, 2, 2], [1, 1, 0]] or grid == [[2, 2, 1], [0, 1, 0], [2, 1, 1]] or grid == [[2, 2, 1], [0, 1, 1], [2, 1, 0]] or grid == [[2, 1, 2], [0, 1, 0], [1, 2, 1]] or grid == [[2, 1, 2], [0, 1, 1], [1, 2, 0]] or grid == [[2, 1, 1], [0, 1, 0], [2, 2, 1]] or grid == [[0, 1, 1], [0, 2, 2], [2, 1, 1]] or grid == [[1, 0, 1], [0, 2, 2], [2, 1, 1]] or grid == [[1, 2, 0], [0, 2, 1], [1, 1, 2]] or grid == [[1, 0, 2], [0, 2, 1], [1, 1, 2]] or grid == [[1, 2, 1], [0, 2, 0], [1, 1, 2]] or grid == [[1, 2, 1], [0, 2, 1], [0, 1, 2]] or grid == [[1, 1, 2], [0, 2, 1], [1, 0, 2]] or grid == [[2, 1, 1], [0, 2, 2], [0, 1, 1]] or grid == [[2, 1, 1], [0, 2, 2], [1, 0, 1]] or grid == [[1, 1, 2], [0, 2, 0], [1, 2, 1]] or grid == [[1, 2, 1], [0, 2, 2], [0, 1, 1]]:
                        grid[1][0] = 2
                    elif grid == [[1, 2, 1], [1, 2, 2], [0, 1, 0]] or grid == [[2, 1, 1], [2, 1, 0], [0, 2, 1]] or grid == [[2, 2, 1], [1, 1, 2], [0, 1, 0]] or grid == [[2, 1, 0], [2, 1, 1], [0, 2, 1]] or grid == [[2, 1, 1], [2, 1, 1], [0, 2, 0]] or grid == [[2, 1, 1], [1, 1, 2], [0, 2, 0]] or grid == [[2, 1, 2], [1, 2, 1], [0, 0, 1]] or grid == [[1, 1, 2], [0, 2, 1], [0, 1, 2]] or grid == [[1, 0, 2], [1, 2, 1], [0, 1, 2]] or grid == [[1, 2, 1], [1, 2, 0], [0, 1, 2]] or grid == [[2, 0, 1], [1, 2, 2], [0, 1, 1]] or grid == [[2, 1, 1], [1, 2, 2], [0, 0, 1]] or grid == [[1, 1, 2], [0, 2, 1], [0, 2, 1]] or grid == [[1, 1, 2], [1, 2, 0], [0, 2, 1]]:
                        grid[2][0] = 2
                    elif grid == [[1, 2, 0], [1, 2, 1], [2, 1, 0]] or grid == [[2, 1, 0], [2, 1, 0], [1, 2, 1]] or grid == [[2, 2, 0], [1, 1, 2], [0, 1, 1]] or grid == [[2, 2, 0], [1, 1, 2], [1, 1, 0]] or grid == [[2, 1, 0], [2, 1, 1], [1, 2, 0]] or grid == [[2, 1, 0], [1, 1, 2], [0, 2, 1]] or grid == [[2, 1, 0], [1, 1, 2], [1, 2, 0]] or grid == [[0, 2, 0], [1, 2, 1], [2, 1, 1]] or grid == [[1, 2, 0], [1, 2, 0], [2, 1, 1]] or grid == [[0, 1, 0], [2, 2, 1], [1, 2, 1]] or grid == [[2, 1, 0], [1, 2, 0], [2, 1, 1]] or grid == [[2, 1, 0], [1, 2, 1], [2, 0, 1]] or grid == [[1, 1, 0], [2, 2, 1], [1, 0, 2]] or grid == [[1, 1, 0], [2, 2, 1], [1, 2, 0]] or grid == [[1, 2, 0], [0, 2, 1], [2, 1, 1]]:
                        grid[0][2] = 2
                    elif grid == [[1, 2, 1], [0, 2, 1], [2, 1, 0]] or grid == [[2, 0, 2], [1, 1, 2], [1, 1, 0]] or grid == [[2, 1, 2], [1, 1, 2], [1, 0, 0]] or grid == [[2, 1, 1], [0, 1, 1], [2, 2, 0]] or grid == [[2, 1, 1], [1, 1, 0], [2, 2, 0]] or grid == [[2, 1, 1], [1, 2, 0], [2, 1, 0]] or grid == [[2, 0, 1], [1, 2, 1], [2, 1, 0]] or grid == [[2, 1, 1], [1, 2, 2], [0, 1, 0]] or grid == [[2, 0, 1], [1, 2, 2], [1, 1, 0]]:
                        grid[2][2] = 2
                    elif grid == [[1, 0, 1], [2, 2, 1], [1, 2, 0]] or grid == [[2, 0, 2], [1, 1, 2], [1, 0, 1]] or grid == [[2, 0, 2], [1, 1, 2], [1, 0, 1]] or grid == [[2, 0, 2], [1, 1, 2], [0, 1, 1]] or grid == [[2, 0, 0], [1, 1, 2], [2, 1, 1]] or grid == [[2, 0, 2], [2, 1, 1], [1, 0, 1]] or grid == [[2, 0, 2], [2, 1, 1], [1, 1, 0]] or grid == [[2, 0, 1], [1, 1, 2], [2, 0, 1]] or grid == [[2, 0, 1], [1, 1, 2], [2, 1, 0]] or grid == [[2, 0, 0], [1, 2, 1], [1, 2, 1]] or grid == [[2, 0, 1], [1, 2, 0], [1, 2, 1]] or grid == [[1, 0, 0], [2, 2, 1], [1, 1, 2]] or grid == [[0, 0, 1], [1, 2, 2], [2, 1, 1]] or grid == [[2, 0, 2], [1, 2, 1], [1, 0, 1]] or grid == [[2, 0, 2], [1, 2, 1], [0, 1, 1]] or grid == [[0, 0, 2], [1, 2, 1], [1, 2, 1]] or grid == [[1, 0, 2], [0, 2, 1], [1, 2, 1]] or grid == [[1, 0, 1], [1, 2, 2], [0, 2, 1]] or grid == [[0, 0, 1], [1, 2, 2], [1, 2, 1]] or grid == [[1, 0, 0], [2, 2, 1], [1, 2, 1]]:
                        grid[0][1] = 2
                    elif grid == [[0, 1, 2], [0, 2, 1], [1, 1, 2]] or grid == [[0, 2, 0], [1, 2, 1], [1, 1, 2]] or grid == [[0, 2, 1], [1, 2, 1], [0, 1, 2]] or grid == [[0, 2, 1], [1, 2, 0], [1, 1, 2]] or grid == [[0, 2, 1], [0, 2, 1], [1, 1, 2]] or grid == [[0, 1, 1], [1, 2, 2], [0, 2, 1]] or grid == [[0, 1, 1], [2, 2, 1], [1, 0, 2]] or grid == [[0, 1, 0], [2, 2, 1], [1, 1, 2]] or grid == [[0, 1, 2], [1, 2, 0], [1, 2, 1]] or grid == [[0, 1, 2], [0, 2, 1], [1, 2, 1]] or grid == [[0, 1, 2], [1, 2, 1], [1, 0, 2]]:
                        grid[0][0] = 2
                    turn -= 1
                    print (grid)
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # --- Drawing code should go here
    if home_screen == 0:
        screen.blit(background_image_homescreen, [0,0])
        drawMultiplayerButton()
        screen.blit(homescreen_image, [175,115])
    elif home_screen == 3:
        screen.blit(how_to_play, [0,0])
        drawExitButton(580,601,615,610)
        screen.blit(example_image, [0,85])
        screen.blit(how_to_play_title, [0,0])
        screen.blit(how_to_play_instructions, [0,455])
    else:
        result = game_screen(home_screen, won_game, winner_param) #design game based on game type
        won_game = result[0]
        winner_param = result[1]

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
