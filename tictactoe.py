from random import randrange

def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    # print("+-------+-------+-------+\n" \
    #       "|       |       |       |\n" \
    #       "|   {}   |   {}   |   {}   |".format(numberOnBoard[0],numberOnBoard[1],numberOnBoard[2]))
    
    # print("|       |       |       |\n" \
    #       "+-------+-------+-------+\n" \
    #       "|       |       |       |\n" \
    #       "|   {}   |   {}   |   {}   |".format(numberOnBoard[3],numberOnBoard[4],numberOnBoard[5]))
    
    # print("|       |       |       |\n" \
    #       "+-------+-------+-------+\n" \
    #       "|       |       |       |\n" \
    #       "|   {}   |   {}   |   {}   |".format(numberOnBoard[6],numberOnBoard[7],numberOnBoard[8]))

    # print("|       |       |       |\n" \
    #       "+-------+-------+-------+")


   
    
#def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

#def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

#def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

#def DrawMove(board):
#
# the function draws the computer's move and updates the board
#

gameEnded = False

for i in range (12):
    for j in range (25):
        

userMoveList = []
comMoveList = []

while not gameEnded:
    DisplayBoard(gameEnded)

    userMove = input("Enter your move: ")

