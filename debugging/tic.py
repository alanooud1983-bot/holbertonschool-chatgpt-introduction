#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the board.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Returns:
    str: 'X' if X wins, 'O' if O wins, None if no winner
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    """
    Check if the board is completely filled.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Players will take turns. Enter row and column (0-2) separated by space.")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row, col = map(int, input("Enter row and column (0-2): ").split())
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Error: Row and column must be between 0 and 2.")
                continue
                
            if board[row][col] != " ":
                print("Error: That position is already taken. Choose another.")
                continue
                
            # Make the move
            board[row][col] = current_player
            
            # Check for winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
                
            # Check for tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
                
            # Switch players
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Error: Please enter two numbers separated by space.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break

if __name__ == "__main__":
    tic_tac_toe()
