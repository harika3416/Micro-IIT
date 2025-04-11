import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, symbol):
    # Check rows and columns
    for i in range(3):
        if all([cell == symbol for cell in board[i]]) or \
           all([board[j][i] == symbol for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol or \
       board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

def computer_move(board):
    # Try to find an empty space randomly
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)
    
    players = ["X", "O"]
    moves = 0
    while moves < 9:
        if moves % 2 == 0:
            # Human player's turn
            current_player = players[0]
            print(f"Player {current_player}'s turn.")
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2 separated by space): ").split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                else:
                    print("That square is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")
                continue
        else:
            # Computer player's turn
            current_player = players[1]
            print(f"Computer ({current_player})'s turn.")
            row, col = computer_move(board)
            board[row][col] = current_player
            print(f"Computer chose row {row}, column {col}.")
        
        # Display the board and check for a winner
        display_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return
        moves += 1

    print("It's a draw!")

# Run the game
tic_tac_toe()