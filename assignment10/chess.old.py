from os import system, name

PIECES = {
    'ivory': '♜♝♞♛♚♟',
    'ebony': '♖♗♘♕♔♙'
}

KNIGHT_DELTAS = [
    (-2, -1),
    (-2, +1),
    (+2, -1),
    (+2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2)
]

PIECE_NAMES = {
    'pawn': '♟♙',
    'rook': '♜♖',
    'bishop': '♝♗',
    'knight': '♞♘',
    'king': '♛♕',
    'queen': '♚♔'
}

blank_board = [
    ['♖', '♗', '♘', '♕', '♔', '♘', '♗', '♖'],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    ['♜', '♝', '♞', '♛', '♚', '♞', '♝', '♜']
]

BOARD = blank_board




def print_board(board = BOARD):
    i = 8
    print('    A B C D E F G H\n')
    for row in board:
        row_str = ' '.join(row)
        print(i, '  ' + row_str + '  ', i)
        i -= 1
    print('\n    A B C D E F G H')


def clear():
    if name == 'nt': # windows
        _ = system('cls')
    else:  # unix (posix)
        _ = system('clear')

def get_players():
    p1 = input('Player 1 (Ivory), Please enter your name: ')
    p2 = input('Player 2 (Ebony), Please enter your name: ')
    return [p1, p2]

def get_move(player):
    move_str = input(player + ', enter your move (C1 B3) : ')
    move_pos = move_str.split()
    return move_pos

def check_legal(move, player):
    try:
        # Syntax-check
        if len(move) != 2:
            return False
        if len(move[0]) != 2 or len(move[1]) != 2:
            return False
        for pos in move:
            indexes = list(pos)
            if indexes[0].lower() not in 'abcdefgh':
                return False
            if 1 > int(indexes[1]) > 8:
                return False

        # Move legal for piece
        # Space occupied

        # Piece to move
        p = get_piece(move[0])
        if p == '.':
            return False
        if player == PLAYERS[0]:
            color = 'ivory'
        elif player == PLAYERS[1]:
            color = 'ebony'
        else:
            return False

        if p not in PIECES[color]:
            return False

        print("piece OK")

        # Sace occupied
        d = get_piece(move[1])
        if d != '.':
            if d in PIECES[color]:
                return False

        # Check if legal movement
        if p in PIECE_NAMES['knight']:
            return check_move_knight(move)
        elif p in PIECE_NAMES['pawn']:
            return check_move_pawn(move, color)
        elif p in PIECE_NAMES['rook']:
            return check_move_rook(move)
        elif p in PIECE_NAMES['bishop']:
            return check_move_bishop
        elif p in PIECE_NAMES['queen']:
            return check_move_queen
        elif p in PIECE_NAMES['king']:
            return check_move_king

        return True
    except:
        return False

def get_index(position):
    alpha = "abcdefgh"
    x = alpha.find(position[0].lower())
    y = 7 - (int(position[1]) - 1)

    return [x, y]


def set_piece(position, piece):
    index = get_index(position)

    x = index[0]
    y = index[1]

    BOARD[y][x] = piece

def get_piece(position):
    try:
        index = get_index(position)

        x = index[0]
        y = index[1]

    except:
        x = position[0]
        y = position[1]

    piece = BOARD[y][x]
    return piece

def replace_piece(move):
    p = get_piece(move[0])
    set_piece(move[0], '.')
    set_piece(move[1], p)


def check_check(board):
    return None


def check_check_mate(board):
    if not check_check(board):
        return False

def get_delta(move):
    frm = get_index(move[0])
    to = get_index(move[1])

    delta = (frm[0] - to[0], frm[1] - to[1])
    return delta


def is_diagonal(move):
    delta = get_delta(move)
    if abs(delta[0]) == abs(delta[1]):
        return True
    return False

def is_straight(move):
    delta = get_delta(move)
    if delta[0] == 0 or delta[1] == 0:
        return True
    return False

def check_clear_path(move):
    if is_diagonal or is_straight:
        delta = get_delta(move)
        frm = get_index(move[0])
        to = get_index(move[1])

        if delta[1] == 0:
            if abs(delta[0]) > 0:
                path = BOARD[frm[1]][frm[0]+1:to[0]]
                print(path)
                for i in range(len(path)):
                    if get_piece([frm[1], i]) != '.':
                        return False

def check_move_knight(move):
    delta = get_delta(move)

    print("delta:", delta)
    if delta in KNIGHT_DELTAS:
        return True
    else:
        return False

def check_move_pawn(move, color):
    return True

def main():
    # Setup
    clear()
    global PLAYERS
    PLAYERS = get_players()
    clear()
    print_board()

    # Game Loop
    while True:
        for player in PLAYERS:
            while True:
                move = get_move(player)
                if check_legal(move, player):
                    check_clear_path(move)
                    replace_piece(move)
                    clear()
                    print_board()
                    break
                print('ILLEGAL MOVE')


main()
