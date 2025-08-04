import math

# Initialize the empty board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(3):
        print(' | '.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('---------')

# Check for winner
def check_winner(player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Check for draw
def is_full():
    return ' ' not in board

# Minimax algorithm
def minimax(depth, is_maximizing):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# AI chooses the best move
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The AI is O.")
    print("Positions are as follows:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8\n")

    print_board()

    while True:
        # Player move
        try:
            move = int(input("\nEnter your move (0–8): "))
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        board[move] = 'X'
        print("\nYour move:")
        print_board()

        if check_winner('X'):
            print("\nYou win!")
            break
        elif is_full():
            print("\nIt's a draw!")
            break

        # AI move
        ai_move()
        print("\nAI's move:")
        print_board()

        if check_winner('O'):
            print("\nAI wins!")
            break
        elif is_full():
            print("\nIt's a draw!")
            break

# Start the game
play_game()