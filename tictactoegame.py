import pygame
import random

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Global Variables
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

# Current player
current_player = 1

# Game is still going
game_still_going = True

# Winner
winner = None

# Draw
draw = False


# Display the game board to the screen
def display_board():
    # This function displays the game board to the screen

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the grid lines
    # Vertical lines
    pygame.draw.line(screen, WHITE, [100, 0], [100, 300], 5)
    pygame.draw.line(screen, WHITE, [200, 0], [200, 300], 5)

    # Horizontal lines
    pygame.draw.line(screen, WHITE, [0, 100], [300, 100], 5)
    pygame.draw.line(screen, WHITE, [0, 200], [300, 200], 5)

    # Display player 1's pieces
    for i in range(3):
        for j in range(3):
            if board[i * 3 + j] == 1:
                pygame.draw.circle(screen, GREEN, [(100 * j) + 50, (100 * i) + 50], 40, 5)

    # Display player 2's pieces
    for i in range(3):
        for j in range(3):
            if board[i * 3 + j] == 2:
                pygame.draw.line(screen, RED, [(100 * j) + 10, (100 * i) + 10], [(100 * j) + 90, (100 * i) + 90], 5)
                pygame.draw.line(screen, RED, [(100 * j) + 90, (100 * i) + 10], [(100 * j) + 10, (100 * i) + 90], 5)

    # Update the screen
    pygame.display.flip()


def play_game():
    # This function plays the game

    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # Handle a turn
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == 1 or winner == 2:
        print(winner, "won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    # This function handles a single turn of an arbitrary player

    # Get position from player
    print(player, "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == 0:
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


def check_if_game_over():
    # This function checks if the game is over

    # Check for a winner
    check_for_winner()

    # Check for a tie
    check_for_tie()


def check_for_winner():
    # This function checks if someone has won

    # Set global variables
    global winner

    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    # This function checks the rows for a win

    # Set global variables
    global game_still_going

    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != 0
    row_2 = board[3] == board[4] == board[5] != 0
    row_3 = board[6] == board[7] == board[8] != 0

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None


def check_columns():
    # This function checks the columns for a win

    # Set global variables
    global game_still_going

    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != 0
    column_2 = board[1] == board[4] == board[7] != 0
    column_3 = board[2] == board[5] == board[8] != 0

    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


def check_diagonals():
    # This function checks the diagonals for a win

    # Set global variables
    global game_still_going

    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != 0
    diagonal_2 = board[2] == board[4] == board[6] != 0

    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


def check_for_tie():
    # This function checks if there is a tie

    # Set global variables
    global game_still_going

    # If board is full
    if 0 not in board:
        game_still_going = False
        return True

    # Else there is no tie
    else:
        return False


def flip_player():
    # This function flips the current player from 1 to 2, or 2 to 1

    # Global variables we need
    global current_player

    # If the current player was 1, make it 2
    if current_player == 1:
        current_player = 2

    # Or if the current player was 2, make it 1
    elif current_player == 2:
        current_player = 1


# Start game
play_game()
