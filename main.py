import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

###################
win = 1
draw = -1
running = 0
###########################
game = running



# This Function Draws Game Board
def draw_board():
    print(" %c| %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# This Function Checks position is empty or not



# This Function Checks player has won or not
def check_win():
    global game
    # Horizontal winning condition
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        game = win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        game = win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        game = win
        # Vertical Winning Condition
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        game = win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        game = win
        # Diagonal Winning Condition
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        game = win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        game = win
        # Match Tie or Draw Condition
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        game = draw
    else:
        game = running


def main():
    draw_board()
    check_win()
    player = 1

    def check_position(x):
        if board[x] == ' ':
            return True
        else:
            return False

    print("Tic-Tac-Toe Game ")
    print("Player 1 [X] --- Player 2 [O]\n")
    print()
    print()
    print("Please Wait...")
    time.sleep(3)
    while game == running:
        os.system('cls')
        draw_board()
        if player % 2 != 0:
            print("Player 1's chance")
            mark = 'X'
        else:
            print("Player 2's chance")
            mark = 'O'
        choice = int(input("Enter the position between [1-9] where you want to mark : "))
        if check_position(choice):
            board[choice] = mark
            player += 1
            check_win()

    os.system('cls')
    draw_board()
    if game == draw:
        print("Game Draw")
    elif game == win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")

    def con():
        inp = input("do u want to continue y or no")
        if inp == 'y' or 'Y':
            main()
        else:
            exit()
    con()

main()


