import math

# Initialize board
board = [" " for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print()

# Check winner
def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(b[i] == player for i in condition) for condition in win_conditions)

# Check draw
def is_draw(b):
    return " " not in b

# Minimax with Alpha-Beta Pruning
def minimax(b, depth, alpha, beta, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                eval = minimax(b, depth + 1, alpha, beta, False)
                b[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                eval = minimax(b, depth + 1, alpha, beta, True)
                b[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI move
def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"

# Human move
def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid position! Choose 1-9.")
            elif board[pos] != " ":
                print("Position already taken!")
            else:
                board[pos] = "X"
                break
        except ValueError:
            print("Please enter a valid number!")

# Game loop
def play_game():
    print("🎮 Tic-Tac-Toe: You (X) vs AI (O)")
    print("Positions are numbered 1 to 9:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    print_board()

    while True:
        # Human turn
        human_move()
        print_board()

        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        # AI turn
        print("🤖 AI is thinking...")
        ai_move()
        print_board()

        if check_winner(board, "O"):
            print("💻 AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()