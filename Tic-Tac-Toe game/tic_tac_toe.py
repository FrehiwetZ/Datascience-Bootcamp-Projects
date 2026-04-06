def print_board(boad):
    print('\n')
    for i in range (3):
        print(" | ".join(board[i]))
        if i < 2:
            print ("--+---+--")
        print('\n')

def check_winner(board, player):
    #check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    #check columns
    for col in range (3):
        if all(board[row][col] == player for row in range (3)):
            return True
    
    #check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
        return True
    
def tic_tac_toe():
    #create an empty board
    board = [[ " " for _ in range (3)] for _ in range (3)]
    
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter row and column (1-3 1-3): ")
            row, col = map(int, move.split())

            # Convert to 0-based index
            row -= 1
            col -= 1

            # Validate move
            if row not in range(3) or col not in range(3):
                print("Invalid position. Try again.")
                continue

            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

            # Make move
            board[row][col] = current_player

            # Check win
            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            # Check draw
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Enter two numbers like: 1 2")


# Run the game
tic_tac_toe()