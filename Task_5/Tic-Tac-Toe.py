board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

player1 = input("Player 1, choose X or O: ").upper()
player2 = "O" if player1 == "X" else "X"

current_player = player1

while True:
    print_board()

    try:
        move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        if move < 0 or move > 8:
            print("❌ Choose number between 1 and 9!")
            continue
    except:
        print("❌ Invalid input! Enter a number.")
        continue

    if board[move] != " ":
        print("⚠️ choose another place.")
        continue

    board[move] = current_player

    if check_winner(current_player):
        print_board()
        print(f"🎉🎉 Player {current_player} WINS 🎉🎉")  

    elif check_draw():
        print_board()
        print("🤝 It's a draw!")
    else:
        
        current_player = player2 if current_player == player1 else player1
        continue

    again = input("Do you want to play again? (y/n): ").lower()

    if again == "y":
        board = [" " for _ in range(9)]
        current_player = player1
        continue
    else:
        print("❤️ Thanks for playing!")
        break