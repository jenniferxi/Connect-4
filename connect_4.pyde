mode = "instruction" # beginning mode\

score_limit = 1000
score_1 = 0 # player 1 score
score_2 = 0 # player 2 score
win1 = 0 # player 1 wins a round
win2 = 0 # player 2 wins a round
victory1 = 0 # player 1 reaches score limit, win the game
victory2 = 0 # player 2 reaches score limit, win the game

turn = 1 # turn 1 is p1, turn 2 is p2
moves = 0 # counts how many moves

animat_dx = 3 # movement of animated text
animat_x = 10 # position of x-coord of animated text

board = [[0, 0, 0, 0, 0, 0, 0] ,
         [0, 0, 0, 0, 0, 0, 0] ,
         [0, 0, 0, 0, 0, 0, 0] ,
         [0, 0, 0, 0, 0, 0, 0] ,
         [0, 0, 0, 0, 0, 0, 0] ,
         [0, 0, 0, 0, 0, 0, 0] ]

def setup():
    size(950,600)
    background(211) # grey bg
    
def draw():
    global mode, board, turn
    global win1,win2
    global victory1, victory2
    global score_1, score_2, text_score_1, text_score_2
    global animat_x, animat_dx
    
    instruction() # welcome screen w/ instructions
    
    if mode == "game": # main game interface
        background(200,200,200)
        fill(31,73,125)
        textSize(40)
        # score count
        fill(54, 169, 255) #Blue
        text("Player 1",750,100) #Player 1 Score text
        text("Player 2",750,200) #Player 2 Score text
        # score counter
        textSize(30)
        text(score_1,750,150)
        text(score_2,750,250)
        textSize(32)
        text("Player", 750, 400)
        text("turn", 750, 500)
        fill (255, 42, 18) #Red
        textSize(40)
        text (str(turn), 775, 450) # Variable turn converted and printed as string
        draw_gameboard()

    if mode == "game over": # score limit is reached
        background(211)
        textSize(80)
        fill(54, 169, 255)
        text("Congratulations!", animat_x + animat_dx, 150, 700, 100,) # text moves back and forth
        if animat_x > 320 or animat_x < 0:
            animat_dx = animat_dx * -1
        animat_x += animat_dx
        
        textSize(50)
        if score_1 == score_limit:#player 1's win
            text("Player 1 is the winner!",210,350)
        elif score_2 == score_limit:#player 2's win
            text("Player 2 is the winner!",210,350)
        textSize(30)
        text("Press E to play again!", 330, 500)
        decoration()
        
############################## FUNCTIONS ############################## 
def reset_game(): # reset variables after each round/game ends
    global board, turn, mode, score_1, score_2, moves
    mode = "game"
    
    board = [ [0,0,0,0,0,0,0], 
             [0,0,0,0,0,0,0], 
             [0,0,0,0,0,0,0], 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0] ]
    turn = 1
    score_1 = 0
    score_2 = 0
    moves = 0
##############################
def instruction(): # welcome screen w/ instructions
    global mode
    if mode == "instruction": 
        textSize(55)
        fill(50,130,255) # blue
        text ("Welcome to Connect 4!",150,100)
        textSize(35)
        text ("INSTRUCTIONS",370,175)
        textSize(25)
        # instructional text
        text ("1. Two players will first decide on a score",120,220)
        text ("2. To drop a piece, click on a space on the bord",120,260)
        text ("3. First player to connect 4 in any direction wins the round",120,300)
        text ("4. First player to reach score limit wins the game",120,340)
        text ("5. A tie game will occur when there is no winner and", 120, 380)
        text ("    there are no moves left to make in the board.", 120, 420)
        text ("6. To start, enter a score limit from 1-9 by pressing the" ,120,460)
        text ("   respective number on the keyboard.",130,500)
        # decorate with the game pieces in corners
        decoration()
##############################
def decoration(): # draws the game pieces in the corners of instruction and victory screen
    # decoration
    fill (255,247, 0) #Dark Yellow
    # top left
    ellipse (80, 80, 100, 100) #Outer layer for yellow piece
    # bottom right
    ellipse (870, 520, 100, 100) #Outer layer for yellow piece
    fill (255, 251, 116) #Lighter yellow
    # top left
    ellipse (80, 80, 80, 80) #Inner layer for yellow piece
    # bottom right
    ellipse (870, 520, 80, 80) #Inner layer for yellow piece
    fill (255, 42, 18) #Dark red
    # top right
    ellipse (870, 80, 100, 100) #Outer layer for red piece
    # bottom left
    ellipse (80, 520, 100, 100) #Outer layer for red piece
    fill (255, 86, 67) #Lighter red
    # top right
    ellipse (870, 80, 80, 80) #Inner layer for red piece
    # bottom left
    ellipse (80, 520, 80, 80) #Inner layer for red piece    
##############################    
def draw_gameboard(): #Drawing game board
    for y in range(6):
        for x in range(7):
            fill (20, 88, 162) #Colour
            rect(x*100,y*100,100,100)
            stroke(0)
            if board[y][x] == 2:
                fill(255,42,18) # dark red
                ellipse(x*100+50,y*100+50,100,100) # outer layer
                fill(255,86,67) # light red
                ellipse(x*100+50,y*100+50,80,80) # inner layer
            elif board[y][x] == 1:
                fill(255,247,0) # dark yellow
                ellipse(x*100+50,y*100+50,100,100) # outer layer
                fill(255, 251, 116) # light yellow
                ellipse(x*100+50,y*100+50,80,80)
##############################        
def find_winners():
    global winner, mode, board, turn, score_1, score_2, moves
    winner = "tie"
    # rows
    for x in range(4): # 7 columns to go through
        for y in range(6): # 6 rows to go through
            if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3] != 0:
                game_over_mode()
    # columns
    for x in range(7): # 7 xumns to go through
        for y in range(3): # 6 ys to go through
            if board[y][x] == board[y+1][x] and board[y][x] == board[y+2][x] and board[y][x] == board[y+3][x] and board[y][x] != 0:
                game_over_mode()
    # top right -> bottom left diagonal
    for y in range(3):
        for x in range(4, 2, -1):
            if board[y][x] == board[y+1][x-1] and board[y][x] == board[y+2][x-2] and board[y][x]==board[y+3][x-3] and board[y][x] != 0:
                game_over_mode()
    # top left -> bottom right diagonal 
    for y in range(3):
        for x in range(4):
            if board[y][x] == board [y+1][x+1] and board[y][x]== board[y+2][x+2] and board[y][x] == board [y+3][x+3] and board[y][x] != 0:
                game_over_mode()
    # no wins
    return False
##############################
def game_over_mode(): # after winner is found, changes mode to victory screen
    global turn, board, score_1, score_2, moves, score_limit, mode
    if turn == 2: # if it was player 2's turn next, that means player 1 won
        score_1 += 1 # add point to score
        board = [[0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ]
        turn = 1
        moves = 0
        if score_1 == score_limit:
            mode = "game over"
    elif turn == 1: # if it was player 1's turn next, that means player 2 won
        score_2 += 1
        board = [[0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ,
                [0, 0, 0, 0, 0, 0, 0] ]
        turn = 1
        moves = 0
        if score_2 == score_limit:
            mode = "game over"
##############################    
def tie(): # checking for tie
    global board,turn, mode, moves
    for y in range(6):
        for x in range(7):
            if board[y][x] != 0 and moves == 42: # if all boxes are full and 42 moves have been taken
                board = [[0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0] ]
                turn = 1
                moves = 0
##############################
def switch_turns(): # function to change turns
    global turn, moves
    if turn == 1: # for player 1
        turn = 2 # setting turn to player 2
    elif turn == 2: # for player 2
        turn = 1 # setting turn to player 1
##############################        
def keyPressed():
    global mode
    global score_limit
    global winner1, winner2, victory1, victory2
    
    # player choosing score limit
    if key in '123456789' and key != 0 and mode == "instruction":
        score_limit = int(key)
        mode = "game"
    # start again
    if key in 'eE' and mode == "win" or key in 'eE' and mode == "tie":
        if winner1 == 1 and score_1 != score_limit:
            winner1 = 0
        elif winner2 == 1 and score_2 != score_limit:
            winner1 = 0
        elif score_1 == score_limit:
            mode = "game over"
        elif score_2 == score_limit:
            mode = "game over"
    if key in 'eE' and mode == "game over":
        reset_game()
##############################
def mousePressed():
    global board, turn, score_1, score_2, win1, win2, moves
     
    #print(mouseX/100, mouseY/100)
    #print(board)
    #print(mode)
    
    if 0 < mouseX < 699: 
        x = mouseX/100
        if board[0][x]==0: # check if box is empty
            for y in range(5,-1,-1):
                if board[y][x] == 0:
                    break
            print(y)
            
            # drop piece
            board[y][x] = turn
            moves += 1
            
            # SWITCH TURNS
            switch_turns()
            
            # check for winners
            find_winners() 
            # check for tie
            tie() 
        
        else:
            print("No move") # box is full
            
        
        
            
