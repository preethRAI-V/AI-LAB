import math

board = ["O","O"," ","X"," "," "," "," "," "] 

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def winner():
    lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "draw"

    return None

def minimax(is_max):
    result = winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "draw":
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best

def computer_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

print("Positions:")
print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")

while True:
    print()
    print_board()

    move = int(input("Enter position (0-8): "))

    if board[move] != " ":
        print("Invalid move")
        continue

    board[move] = "X"

    if winner():
        break

    computer_move()

    if winner():
        break

result = winner()

print()
print_board()

if result == "X":
    print("You win!")
elif result == "O":
    print("Computer wins!")
else:
    print("Draw!")
