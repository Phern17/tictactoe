from random import randrange

def DisplayBoard(boardStatus):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print("+-------+-------+-------+\n" \
          "|       |       |       |\n" \
          "|   {}   |   {}   |   {}   |".format(board[0][0],board[0][1],board[0][2]))
    
    print("|       |       |       |\n" \
          "+-------+-------+-------+\n" \
          "|       |       |       |\n" \
          "|   {}   |   {}   |   {}   |".format(board[1][0],board[1][1],board[1][2]))
    
    print("|       |       |       |\n" \
          "+-------+-------+-------+\n" \
          "|       |       |       |\n" \
          "|   {}   |   {}   |   {}   |".format(board[2][0],board[2][1],board[2][2]))

    print("|       |       |       |\n" \
          "+-------+-------+-------+")

def EnterMove(boardStatus):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#   
    userMove = int(input("Enter your move: "))
    pos = 0
        
    for i in range(len(board)):
       if userMove in board[i]:
           pos = board[i].index(userMove)
           board[i][pos] = "O"
           break

    for i in range(len(victory_list)):
        if userMove in victory_list[i]:
            pos = victory_list[i].index(userMove)
            victory_list[i][pos] = "O"
            

    userMoveList.append(userMove)
    print(board)
    DisplayBoard(boardStatus)

#def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(boardStatus, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
    
    for i in range(len(victory_list)):
        counter =  victory_list[i].count(sign)

        if counter == 3:
            boardStatus = True
            return boardStatus
    
        
        


def DrawMove(boardStatus):
#
# the function draws the computer's move and updates the board
#
    randMove = 5

    while randMove in userMoveList or randMove in comMoveList:
        randMove = randrange(1,9)
    
    for i in range(len(board)):
        if randMove in board[i]:
            pos = board[i].index(randMove)
            board[i][pos] = "X"
            break

    for i in range(len(victory_list)):
        if randMove in victory_list[i]:
            pos = victory_list[i].index(randMove)
            victory_list[i][pos] = "X"
            

    print("randMove: " + str(randMove))

    comMoveList.append(randMove)

    DisplayBoard(boardStatus)


gameEnded = False

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

victory_list = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]         
        
userMoveList = []
comMoveList = []
counter = 0

while not gameEnded:
    #computer always make a move first
    DrawMove(gameEnded)
    if VictoryFor(gameEnded, "X"):
        print("U lose!")
        break 
    
    EnterMove(gameEnded)
    if VictoryFor(gameEnded, "O"):
        print("U win!")
        break 
    
