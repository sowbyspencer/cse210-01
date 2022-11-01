#My TicTacToe Game
"""
Author: Spencer Sowby
Assignment: W01 Prove: Developer
"""
# Globasl variables
XOgrid = [[0,0,0],[0,0,0],[0,0,0]]
display = [[1,2,3],[4,5,6],[7,8,9]]
choices = list(range(1, 10))
winner = None

#Variables for formatting
green = "\033[1;32;40m"
default = "\033[0;37;40m"
yellow = "\033[1;33;40m"
red = "\033[1;31;40m"

def printInterface():
    """Prints out the user interface accessing the global lists

    Parameters: none
    Return: none
    """
    print()
    for i in range(0, len(display)):
        line = ""
        for j in range(0, len(display[i])):
            line += f" {display[i][j]} |"
        print(f"{line[:-1]}")
        if i != 2 or j != 2:
            print(f" - + - + -")
    print()

def turn(xo, selection):
    """Records the entry, prints the interface, then checks if there is a winner.

    Parameters:
        xo is "X" or "O". Whos turn it is
        selection is which box was chosen
    Return: none
    """
    # Translates the selection (an integer) to a pair (i and j) to be the row and column selected
    if selection < 4:
        i = 0
        j = selection - 1         
    elif selection < 7:
        i = 1
        j = selection - 4
    elif selection < 10:
        i = 2        
        j = selection - 7

    # Remove the selection from available options
    choices.remove(selection)

    # Change the display list
    if xo == "X":
        color = green
    else:
        color = yellow
    display[i][j] = f"{color}{xo}{default}"

    # Record the entry as a 1 for X, and a - for O
    if xo == "X":
        XOgrid[i][j] = 1
    else:
        XOgrid[i][j] = -1

    # Prints the changes
    printInterface()
    # Checks if there is now a winner
    checkForWin()

def checkForWin():
    """Checks if there is a winner yet

    Parameters: none
       
    Return: none
    """
    # Check rows
    global winner
    for i in XOgrid:
        rowTotal = 0
        for j in i:
            rowTotal += j

        if rowTotal == 3:
            winner = "X"
            return
        elif rowTotal == -3:
            winner = "O"
            return
    
    # Check Columns
    for j in range(0, 3):
        colTotal = 0
        for i in XOgrid:
            colTotal += i[j]
        if colTotal == 3:
            winner = "X"
            return
        elif colTotal == -3:
            winner = "O"
            return

    # Check diagnals
    if XOgrid[0][0] + XOgrid[1][1] + XOgrid[2][2] == 3:
        winner = "X"
        return
    elif XOgrid[0][0] + XOgrid[1][1] + XOgrid[2][2] == -3:
        winner = "O"
        return

    if XOgrid[0][2] + XOgrid[1][1] + XOgrid[2][0] == 3:
        winner = "X"
        return
    elif XOgrid[0][2] + XOgrid[1][1] + XOgrid[2][0] == -3:
        winner = "O"
        return

def main():
    """Allows two players to play a game of Tic-Tac-Toe
    """
    print(choices)
    printInterface()
    
    # Repeat until there is a winner
    while winner == None:
        selection = int(input(f"{green}X{default}'s turn to choose a square (1-9): "))
        while not selection in choices:
            print(f"{red}{selection} is not an option.{default}")
            selection = int(input(f"{green}X{default}'s turn to choose a square (1-9): "))
        turn("X", selection)

        if winner != None:
            break
        elif len(choices) == 0:
            print(f"The Game was a DRAW")
            print(f"Good game. Thanks for playing!")
            return

        selection = int(input(f"{yellow}O{default}'s turn to choose a square (1-9): "))
        while not selection in choices:
            print(f"{red}{selection} is not an option.{default}")
            selection = int(input(f"{yellow}O{default}'s turn to choose a square (1-9): "))
        turn("O", selection)
    
    print(f"The winner is: {winner}")
    print(f"Good game. Thanks for playing!")

if __name__ == "__main__":
    main()