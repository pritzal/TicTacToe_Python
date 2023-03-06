import tkinter as tk

board = [' ' for x in range(9)]
player = 'X'
game_over = False

def make_move(position):
    global player, board, game_over
    if board[position] == ' ' and not game_over:
        board[position] = player
        button = button_list[position]
        button.config(text=player)
        if check_winner(player):
            game_over = True
            message_label.config(text=f'Congratulations, Player {player} wins!')
        elif is_board_full():
            game_over = True
            message_label.config(text='The game is a tie!')
        else:
            player = 'O' if player == 'X' else 'X'
            message_label.config(text=f"Player {player}'s turn")

def check_winner(player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def is_board_full():
    return ' ' not in board

def reset_game():
    global player, board, game_over
    player = 'X'
    board = [' ' for x in range(9)]
    game_over = False
    for button in button_list:
        button.config(text=' ')
    message_label.config(text=f"Player {player}'s turn")

root = tk.Tk()
root.title('Tic Tac Toe')

button_frame = tk.Frame(root)
button_frame.pack()

button_list = []
for i in range(9):
    button = tk.Button(button_frame, text=' ', font=('Arial', 20), width=3, height=1, command=lambda pos=i: make_move(pos))
    button.grid(row=i // 3, column=i % 3)
    button_list.append(button)

message_label = tk.Label(root, text=f"Player {player}'s turn", font=('Arial', 16))
message_label.pack()

reset_button = tk.Button(root, text='Reset Game', font=('Arial', 16), command=reset_game)
reset_button.pack()

root.mainloop()


