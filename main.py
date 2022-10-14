from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")

    for row in board:
        print("|       |       |       |")
        print("|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    new_board = board
    try:
        new_move = int(input("Enter your move: "))
    except ValueError:
        print("Square must be an int between 1 and 9!")
        new_move = None
    if new_move and 1 <= new_move <= 9:
        if 1 <= new_move <= 3:
            new_board[0][new_move - 1] = "O"
        elif 4 <= new_move <= 6:
            new_board[1][new_move - 4] = "O"
        elif 7 <= new_move <= 9:
            new_board[2][new_move - 7] = "O"
    else:
        print("Invalid square, outside of range:", new_move)
        print("Skipping your turn...")
    return new_board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return_me = []
    row_num = 0
    col_num = 0
    for row in board:
        for i in row:
            if i != "X" and i != "O" and type(i) == int:
                return_me.append((row_num, col_num))
            col_num += 1
        row_num += 1
        col_num = 0
    return return_me


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    player_won = False

    # Check for horizontal win
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            player_won = True

    # Check for vertical win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            player_won = True

    # Check for diagonal win
    if board[0][0] == board[1][1] == board[2][2] == sign:
        player_won = True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        player_won = True

    return player_won


def draw_move(board):
    # The function draws the computer's move and updates the board.
    new_board = board
    free_fields = make_list_of_free_fields(board)
    while True:
        computers_move = (randrange(3), randrange(3))
        if computers_move in free_fields:
            new_board[computers_move[0]][computers_move[1]] = "X"
            break

    return new_board


main_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
display_board(main_board)

computers_turn = False
while True:
    if computers_turn:
        # Computer's turn.
        main_board = draw_move(main_board)
        display_board(main_board)
        computers_turn = False
    else:
        # User's turn.
        main_board = enter_move(main_board)
        display_board(main_board)
        computers_turn = True

    if victory_for(main_board, "X"):
        print("Computer won :(")
        break
    elif victory_for(main_board, "O"):
        print("You won!")
        break
    elif len(make_list_of_free_fields(main_board)) == 0:
        print("Tie game.")
        break
