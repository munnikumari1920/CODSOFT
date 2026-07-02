import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw():
    return " " not in board

def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move.")
        except:
            print("Enter a valid number.")

def ai_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"

def play_game():
    print("===== TIC TAC TOE AI =====")
    print("You = X")
    print("AI = O")

    while True:
        print_board()

        human_move()

        if check_winner("X"):
            print_board()
            print("You Win!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break

play_game()