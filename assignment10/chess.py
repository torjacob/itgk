from os import system, name

KNIGHT_DELTAS = [
    (-2, -1),
    (-2,  1),
    ( 2, -1),
    ( 2,  1),
    (-1, -2),
    (-1,  2),
    ( 1, -2),
    ( 1,  2)
]

KING_DELTAS = [
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    (-1,  1),
    (-1,  0),
    (-1, -1),
    ( 0,  1),
    ( 0, -1)
]
PIECES = {
    'ivory': '♜♝♞♛♚♟',
    'ebony': '♖♗♘♕♔♙'
}

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

def clear(): # Clear screen
    if name == 'nt': # windows
        _ = system('cls')
    else:  # unix (posix)
        _ = system('clear')

def print_board(): # Print board to screen
    i = 8
    print('    A B C D E F G H\n')
    for row in BOARD:
        row_str = ' '.join(row)
        print(i, '  ' + row_str + '  ', i)
        i -= 1
    print('\n    A B C D E F G H')

def get_players(): # Fetch names of players
    p1 = input('Player 1 (Ivory), Please enter your name: ')
    p2 = input('Player 2 (Ebony), Please enter your name: ')
    return [p1, p2]

# # # # # # # # # # # # # # # # # LEGEND # # # # # # # # # # # # # # # # # # #
# MOVE: Change in position written in chess-syntax, str - A1 A4 or C3 D3
# POSITION: One part of move, str - A1 or C8
# POS_INDEX: A position based on index in board, [int] - [0, 0] or [3, 7]
# DELTA: Tuplet containing change of index in board, tuplet - (x, y)
# PATH: List of content from squares between to positions, [str] - ['.', '.']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def get_move(player): # Get move from current player
    move_str = input(player + ', enter your move (C1 B3) : ')
    move = move_str.split()
    return move

def get_index(position): # Translate from player move to index in board
    alpha = "abcdefgh"
    x = alpha.find(position[0].lower())
    y = 7 - (int(position[1]) - 1)
    return [x, y]

def get_piece(pos_index): # Fetch piece on given index of board
    x = pos_index[0]
    y = pos_index[1]
    piece = BOARD[y][x]
    return piece

def set_piece(pos_index, piece): # Place piece on given index of board
    x = pos_index[0]
    y = pos_index[1]
    BOARD[y][x] = piece

def move_piece(move): # Move piece around board
    p = get_piece(get_index(move[0]))
    set_piece(get_index(move[0]), '.') # Empty origin
    set_piece(get_index(move[1]), p) # Fill destination

def calc_delta(move): # Calculate change in index of position
    frm = get_index(move[0])
    to = get_index(move[1])
    delta = (frm[0] - to[0], frm[1] - to[1])
    return delta

def is_diagonal(delta): # Check if move is diagonal
    if abs(delta[0]) == abs(delta[1]):
        return True
    return False

def is_straight(delta): # Check if move is straight
    if delta[0] == 0 or delta[1] == 0:
        return True
    return False

# TODO: implement both positive and negative directions
def get_path(move): # Fetch path of move
    # Split up delta, from_index, to_index into x and y components for easier comprehension
    delta = calc_delta(move)
    delta_x = delta[0]
    delta_y = delta[1]

    from_index = get_index(move[0])
    from_x = from_index[0]
    from_y = from_index[1]

    to_index = get_index(move[1])
    to_x = to_index[0]
    to_y = to_index[1]

    if is_straight(delta): # Horizontal or vertical
        if delta_y == 0: # Horizontal
            if delta_x < 0: # L to R
                path = BOARD[from_y][from_x + 1 : to_x]
            else: # R to L
                path = BOARD[from_y][to_x + 1 : from_x]
        elif delta_x == 0: # Vertical
            if delta_y > 0: # B to T
                path = [BOARD[i][from_x] for i in range(to_y + 1, from_y)]
            else: # T to B
                path = [BOARD[i][from_x] for i in range(from_y + 1, to_y)]

    elif is_diagonal(delta): # Diagonal
        if delta_x < 0 and delta_y < 0: # TL to BR
            path = [BOARD[from_y + i][from_x + i] for i in range(1, abs(delta_x))]
        elif delta_x > 0 and delta_y > 0: # BR to TL
            path = [BOARD[from_y - i][from_x - i] for i in range(1, abs(delta_x))]
        elif delta[0] > 0 and delta[1] < 0: # TR to BL
            path = [BOARD[from_y + i][from_x - i] for i in range(1, abs(delta_x))]
        else: # BL to TR
            path = [BOARD[from_y - i][from_x + i] for i in range(1, abs(delta_x))]

    else: # Jump (Knight)
        path = ['.'] # TRUE

    # Movement info: Debugging
    print('from_index:', from_index, 'to_index:', to_index)
    print('delta:', delta)
    print('path:', path)

    return path

def check_clear_path(path): # Check if path is clear
    for i in range(len(path)): # Look through path for pieces
        if path[i] != '.':
            return False

def check_move_pawn(move, color): # Check if move is within moveset -- PAWN
    delta = calc_delta(move)
    delta_x = delta[0]
    delta_y = delta[1]
    max_delta_y = 1
    from_y = get_index(move[0])[1]
    print(delta_x)

    dest_piece = get_piece(get_index(move[1]))

    if (color == 'ebony' and from_y == 1) or (color == 'ivory' and from_y == 6): # Start position
        max_delta_y = 2

    if abs(delta_x) == 0:
        if (color == 'ebony' and delta_y > 0) or (color == 'ivory' and delta_y < 0):
            return False
        if abs(delta_y) > max_delta_y:
            return False

    if abs(delta_x) == 1: # Strike
        if check_piece_color(dest_piece, color) or dest_piece == '.':
            return False

    if abs(delta_x) > 1:
        return False

    return True

def check_swap_pawn(pos_index, color):
    pos_y = pos_index[1]
    print(pos_index)

    if (color == 'ebony' and pos_y == 7) or (color == 'ivory' and pos_y == 0):
        piece = get_input_piece(color)
        set_piece(pos_index, piece)

def get_input_piece(color):
    valid_names = 'rbkq'
    while True:
        p_name = input('Choose which piece to transform to (q b k r): ')
        if p_name in valid_names:
            break
        print('Not a valid choice, try again.')

    return PIECES[color][valid_names.index(p_name)]


def check_move_rook(delta): # Check if move is within moveset -- ROOK
    if is_straight(delta):
        return True
    return False

def check_move_knight(delta): # Check if move is within moveset -- KNIGHT
    if delta in KNIGHT_DELTAS:
        return True
    return False

def check_move_bishop(delta): # Check if move is within moveset -- BISHOP
    if is_diagonal(delta):
        return True
    return False

def check_move_queen(delta): # Check if move is within moveset -- QUEEN
    if is_straight(delta) or is_diagonal(delta):
        return True
    return False

def check_move_king(delta): # Check if move is within moveset -- KING
    if delta in KING_DELTAS:
        return True
    return False

def check_check(): # Check if king is in check
    '''
def check_checkmate(): # Check if king is in checkmate (WINNER!)
    if check_check():
        # CHECK FOR MATE
    return False
    '''

def check_piece_color(piece, color): # Does position have a piece on players side?
    if piece in PIECES[color]:
        return True
    return False

def get_player_color(player):
    if player == PLAYERS[0]:
        color = 'ivory'
    else:
        color = 'ebony'
    return color


def check_legal(move, player, color, delta): # Run through all legality / validity checks for move
    global ERROR
    ERROR = ''
    # Syntax check
    if len(move) != 2 or len(move[0]) != 2 or len(move[1]) != 2:
        ERROR = 'Wrong number/length of args'
        return False
    for pos in move:
        indexes = list(pos)
        if indexes[0].lower() not in 'abcdefgh' or 1 > int(indexes[1]) > 8:
            ERROR = 'Cannot find spot on board'
            return False
    # Can player move piece?
    p = get_piece(get_index(move[0]))
    if p == '.' or p not in PIECES[color]: # Does start have a piece on players side?
        ERROR = 'You cannot move that piece'
        return False

    # moveset check for piece
    if p in PIECE_NAMES['pawn']:
        func = check_move_pawn(move, color)
    elif p in PIECE_NAMES['rook']:
        func = check_move_rook(delta)
    elif p in PIECE_NAMES['bishop']:
        func = check_move_bishop(delta)
    elif p in PIECE_NAMES['knight']:
        func = check_move_knight(delta)
    elif p in PIECE_NAMES['queen']:
        func = check_move_queen(delta)
    elif p in PIECE_NAMES['king']:
        func = check_move_king(delta)
    if not func:
        return func

    d = get_piece(get_index(move[1]))
    if d != '.':
        if d in PIECES[color]: # Does destination have a piece on enemy side?
            ERROR = 'Destination already has one of your pieces'
            return False
    if check_clear_path(get_path(move)) == False: # Is the path clear?
        ERROR = 'Movement path is not clear'
        return False

    # Check if move is in moveset of piece

    return True # All checks for legality run

def main(): # Run game
    # Setup
    clear()
    global PLAYERS
    PLAYERS = get_players()
    clear()
    print_board()

    while True: # Game Loop
        for player in PLAYERS:
            while True:
                move = get_move(player)
                delta = calc_delta(move)
                from_pos_index = get_index(move[0])
                to_pos_index = get_index(move[1])
                color = get_player_color(player)
                p = get_piece(from_pos_index)

                if check_legal(move, player, color, delta):
                    move_piece(move)
                    if p in PIECE_NAMES["pawn"]:
                        check_swap_pawn(to_pos_index, color)
                    # If other side of board and pawn -- replace_piece(pos_index, piece)
                    # clear()
                    print_board()
                    break
                print('ILLEGAL MOVE: ' + ERROR)

main()
