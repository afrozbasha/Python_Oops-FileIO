"""
    @Author: Afroz Basha
    @Date: 2021-08-25
    @Title: 2D ARRAY
"""
"""
Description:
   Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 is the Computer and the Player 2 is the user. 
   Player 1 take Random Cell that is the Column and Row.
Parameter:
    Logic Concept Using Try & Except
Return:
   It return the winner between Computer & User
"""

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
play = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running


def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___________")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___________")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))


def checkWins():
    """Checking the winning position to the Tic-Tac-Toe board"""
    global Game
    # checking Horizontal Winning
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
        # checking Vertical Winning
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
        # checking Diagonal Winning
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
        # checking Match Tie or Draw
    elif \
            board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and \
                    board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        print("Game Draw")
        Game = Draw
    else:
        Game = Running


pass


def checkPos(pos):
    """Checking the free position in Tic-Tac-Toe board"""
    if board[pos] == ' ':
        return True
    else:
        return False
    pass


print("Tic-Tac-Toe Game")
print("Player 1 User symbol-> `X` \n"
      "Player 2 Computer symbol -> `O`\n")
while Game == Running:
    DrawBoard()
    if play % 2 != 0:
        print("Player 1 chance to play")
        mark = 'X'
    else:
        print("Player 2 chance to play")
        mark = 'O'
    pos = int(input("Enter the position between [1-9] : "))
    if checkPos(pos):
        board[pos] = mark
        play += 1
        checkWins()
    else:
        print("!Please enter free place position")
DrawBoard()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    play -= 1
    if play % 2 != 0:
        print("Player 1 User Won")
    else:
        print("Player 2 Computer Won")
