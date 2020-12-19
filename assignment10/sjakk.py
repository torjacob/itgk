# Imports ---------------------------------------------------------------------
from os import system, name # for clear function

# Global Vars -----------------------------------------------------------------
DELTAS = {
    'knight' : [
        (-2, -1),
        (-2,  1),
        ( 2, -1),
        ( 2,  1),
        (-1, -2),
        (-1,  2),
        ( 1, -2),
        ( 1,  2)
    ],
    'king' : [
        ( 1,  1),
        ( 1,  0),
        ( 1, -1),
        ( 0,  1),
        ( 0, -1),
        (-1,  1),
        (-1,  0),
        (-1, -1)
    ]
}

PIECES = {
    'ivory': '♜♝♞♛♚♟',
    'ebony': '♖♗♘♕♔♙'
}

PIECE_NAMES = {
    'pawn': '♟♙',
    'rook': '♜♖',
    'bishop': '♝♗',
    'knight': '♞♘',
    'king': '♚♔',
    'queen': '♛♕'
}

standard_board = [
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
]

test_board = [
    ['.', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    ['♟', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
]

chess_test_board = [

    ['♖', '.', '♗', '♕', '♔', '♗', '♘', '♖'],
    ['♙', '♙', '♙', '.', '♙', '♙', '♙', '♙'],
    ['.', '.', '♘', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '♙', '.', '.', '.', '.'],
    ['.', '.', '.', '♟', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['♟', '♟', '♟', '.', '♟', '♟', '♟', '♟'],
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
]

BOARD = test_board

# Functions -------------------------------------------------------------------
# Screen related functions
def clear(): # Clear screen
    if name == 'nt': # windows
        _ = system('cls')
    else:  # unix (posix)
        _ = system('clear')

def print_board(): # Print BOARD to screen with border
    i = len(BOARD)
    print('  A B C D E F G H')
    for row in BOARD:
        row_str = ' '.join(row)
        print(i, row_str, i)
        i -=1
    print('  A B C D E F G H')

# # # # # # # # # # # # # # # # # LEGEND # # # # # # # # # # # # # # # # # # #
# MOVE: Change in position written in chess-syntax, str - A1 A4 or C3 D3
# POSITION: One part of move, str - A1 or C8
# INDEX: A position based on index in board, [int] - [0, 0] or [3, 7]
# DELTA: Tuplet containing change of index in board, tuplet - (x, y)
# PATH: List of content from squares between to positions, [str] - ['.', '.']
# PLAYER: Name of player, str
# PLAYERS: List of PLAYERs, [str]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Get functions
def get_players(): # Fetch name of players through input | -> [str]
    p1 = input('Player 1 (Ivory), Please enter your name: ')
    p2 = input('Player 2 (Ebony), Please enter your name: ')
    return [p1, p2]

def get_color(player): # Get color of player | str -> str
    if player == PLAYERS[0]:
        color = 'ivory'
    else:
        color = 'ebony'
    return color

def get_move(player): # Get move from current player | str -> [str]
    move_str = input(player + ', enter your move (C1 B3) : ')
    move = move_str.split()
    return move

def get_index(position): # Translate from player move to index in board | str -> [int]
    alpha = "abcdefgh"
    x = alpha.find(position[0].lower())
    y = 7 - (int(position[1]) - 1)
    index = [x, y]
    return index

def get_position(index): # Translate from index in board to position | [int] -> str
    alpha = "abcdefgh"
    x = alpha[index[0]]
    y = 8 - index[1]
    position = x + str(y)
    return position

def get_piece(index): # Fetch piece from index on board | [int] -> str
    x = index[0]
    y = index[1]
    piece = BOARD[y][x]
    return piece

def get_input_piece(color): # Fetch piece from user input | str -> str
    valid_names = 'rbkq'
    while True:
        p_name = input('Choose which piece to transform to (q b k r): ')
        if p_name in valid_names:
            break
        print('Not a valid choice, try again.')
    return PIECES[color][valid_names.index(p_name)]

def get_index_piece(piece): # Get index of given piece | str -> [int]
    i = 0
    for row in BOARD:
        j = 0
        for cell in row:
            if cell == piece:
                return [j, i]
            j += 1
        i += 1

def get_index_all_pieces(color): # Get index of all pieces in color | str -> [[int]]
    positions = []
    i = 0
    for row in BOARD:
        j = 0
        for cell in row:
            if cell in PIECES[color]:
                positions.append([j, i])
            j += 1
        i += 1
    return positions

def get_delta(move): # Get delta of move | str -> (int)
    from_index = get_index(move[0])
    to_index = get_index(move[1])
    delta = (from_index[0] - to_index[0], from_index[1] - to_index[1])
    return delta

def get_path(move): # Fetch path of move
    # Split up delta, from_index, to_index into x and y components for easier comprehension
    delta = get_delta(move)
    delta_x = delta[0]
    delta_y = delta[1]

    from_index = get_index(move[0])
    from_x = from_index[0]
    from_y = from_index[1]

    to_index = get_index(move[1])
    to_x = to_index[0]
    to_y = to_index[1]

    if check_straight(delta): # Horizontal or vertical
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

    elif check_diagonal(delta): # Diagonal
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
    # print('from_index:', from_index, 'to_index:', to_index)
    # print('delta:', delta)
    # print('path:', path)

    return path

def get_possible_king_moves(position): # Get possible king moves | str -> str
    king_index = get_index(position)
    moves = []
    for delta in DELTAS['king']:
        calc_pos = [king_index[0] + delta[0], king_index[1] + delta[1]]
        if not(calc_pos[0] < 0 or calc_pos[1] < 0 or calc_pos[0] > 7 or calc_pos[1] > 7):
            moves.append(position + ' ' + get_position(calc_pos))
    return moves

def get_possible_king_to_positions(position): # Get possible king pos from current pos | str -> [str]
    king_index = get_index(position)
    positions = []
    for delta in DELTAS["king"]:
        calc_pos = [king_index[0] + delta[0], king_index[1] + delta[1]]
        if not(calc_pos[0] < 0 or calc_pos[1] < 0 or calc_pos[0] > 7 or calc_pos[1] > 7):
            positions.append(get_position(calc_pos))
    return positions

def get_attacking_piece_positions(position, attacking_color):
    attacking_color_indexes = get_index_all_pieces(attacking_color)
    attacking_piece_positions = []

    for coordinate in attacking_color_indexes:
        attacking_position = get_position(coordinate)
        attacking_move = [attacking_position, position]
        delta = get_delta(attacking_move)
        if check_legal(attacking_move, attacking_color, delta, False):
            attacking_piece_positions.append(attacking_position)

    return attacking_piece_positions



# Set functions
def set_piece(pos_index, piece): # Place piece on given index of board
    x = pos_index[0]
    y = pos_index[1]
    BOARD[y][x] = piece

# Tests - return True or False
# Path related checks
def check_diagonal(delta): # Check if move is diagonal
    if abs(delta[0]) == abs(delta[1]):
        return True
    return False

def check_straight(delta): # Check if move is straight
    if delta[0] == 0 or delta[1] == 0:
        return True
    return False

def check_clear_path(path): # Check if path is clear
    for i in range(len(path)): # Look through path for pieces
        if path[i] != '.':
            return False


# Piece related checks
def check_swap_pawn(index, color): # Check if pawn can be swapped
    y = index[1]
    if (color == 'ebony' and y == 7) or (color == 'ivory' and y == 0):
        return True
    return False

# Move checks
def check_move_pawn(move, color): # Check if move is within moveset -- PAWN
    delta = get_delta(move)
    delta_x = delta[0]
    delta_y = delta[1]
    max_delta_y = 1
    from_y = get_index(move[0])[1]
    # print(delta_x)

    dest_piece = get_piece(get_index(move[1]))

    if (color == 'ebony' and from_y == 1) or (color == 'ivory' and from_y == 6): # Start position
        max_delta_y = 2

    if (color == 'ebony' and delta_y > 0) or (color == 'ivory' and delta_y < 0):
        return False

    if abs(delta_x) > 0:    #if strike only allowed one square vertical
        max_delta_y = 1

    if abs(delta_y) > max_delta_y:
        return False

    if abs(delta_x) == 1 and abs(delta_y) != 1: # Only diagonal, not horizontal
        return False

    if abs(delta_x) == 1: # Strike
        if check_piece_color(dest_piece, color) or dest_piece == '.':
            return False

    if abs(delta_x) > 1:
        return False

    return True

def check_move_rook(delta): # Check if move is within moveset -- ROOK
    if check_straight(delta):
        return True
    return False

def check_move_knight(delta): # Check if move is within moveset -- KNIGHT
    if delta in DELTAS['knight']:
        return True
    return False

def check_move_bishop(delta): # Check if move is within moveset -- BISHOP
    if check_diagonal(delta):
        return True
    return False

def check_move_queen(delta): # Check if move is within moveset -- QUEEN
    if check_straight(delta) or check_diagonal(delta):
        return True
    return False

def check_move_king(delta): # Check if move is within moveset -- KING
    if delta in DELTAS['king']:
        return True
    return False

# Check and checkmate
def check_attack_state(position, attacking_color): # Is the square in question under attack by one of the attacking_colors pieces
    attacking_color_indexes = get_index_all_pieces(attacking_color) # Get list of all attacking colors pieces
    for coordinate in attacking_color_indexes: # Check moves from all of those positions to the position to check
        attacking_position = get_position(coordinate)
        full_move = [attacking_position, position]
        # print('Checking', full_move, ' for position attack')
        delta = get_delta(full_move)
        if check_legal(full_move, attacking_color, delta, False) :
            return True
    return False

def check_threat_king(pos_defending_king, defending_color):
    can_king_handle_threat = False

    if defending_color == 'ebony':
        attacking_color = 'ivory'
    else:
        attacking_color = 'ebony'

    for possible_king_position in get_possible_king_to_positions(pos_defending_king):
        piece_at_position = get_piece(get_index(possible_king_position))
        if not check_piece_color(piece_at_position, defending_color): # Cannot move to position where own piece is
            if not check_attack_state(possible_king_position, attacking_color):
                can_king_handle_threat = True

    if can_king_handle_threat:
        return False

def check_threat_others(pos_defending_king, defending_color):
    #Get list of all pieces threathening defeding king
    if defending_color == 'ebony':
        attacking_color = 'ivory'
    else:
        attacking_color = 'ebony'
    attacking_positions = get_attacking_piece_positions(pos_defending_king, attacking_color)

    if len(attacking_positions) == 0:   #No threaths, would not normally happen
        return False
    if len(attacking_positions) > 1: #Assuming we cannot take out two threaths by one move
        return False
    prime_attacker_position = attacking_positions[0] #get the attacking position
    possible_attack_removers = get_attacking_piece_positions(prime_attacker_position, defending_color)
    try:
        king_pos_index = possible_attack_removers.index(pos_defending_king)
        del possible_attack_removers[king_pos_index]
    except:
        None

    if len(possible_attack_removers) > 0 :
        return True
    return False

def check_check(color): # Check if king is in check
    pos_defending_king = get_position(get_index_piece(PIECES[color][4])) # Fetch pos_index of king

    if color == 'ebony':
        attacking_color = 'ivory'
    else:
        attacking_color = 'ebony'

    retval = check_attack_state(pos_defending_king, attacking_color)
    # print('Under attack : ', retval)
    return retval

def check_checkmate(color): # Check if king is in checkmate (WINNER!)
    pos_defending_king = get_position(get_index_piece(PIECES[color][4])) # Fetch pos_index of king
    if check_threat_king(pos_defending_king, color) or check_threat_others(pos_defending_king, color):
        return False
    return True

def check_piece_color(piece, color): # Does position have a piece on players side?
    if piece in PIECES[color]:
        return True
    return False

# Legality check
def check_legal(move, color, delta, check_target_position): # Run through all legality / validity checks for move
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
    if p not in PIECES[color]: # Does start have a piece on players side?
        if p == '.':
            ERROR = 'That cell is empty'
        else:
            ERROR = 'You cannot move that piece'
        return False

    # Moveset check for piece
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
        ERROR = 'That\'s not a legal move for that piece'
        return func

    # Is the destination valid?
    d = get_piece(get_index(move[1]))
    if d != '.':
        if check_target_position: # Not checking for piece in square when doing attack checks
            if d in PIECES[color]: # Does destination have a piece on enemy side?
                ERROR = 'Destination already has one of your pieces'
                return False
    if check_clear_path(get_path(move)) == False: # Is the path clear?
        ERROR = 'Movement path is not clear'
        return False
    return True # All checks for legality run

# Other functions
def move_piece(move): # Move piece around board
    p = get_piece(get_index(move[0]))
    set_piece(get_index(move[0]), '.') # Empty origin
    set_piece(get_index(move[1]), p) # Fill destination

def swap_pawn(index, color): # Swap pawn from player input when crossing board
    piece = get_input_piece(color)
    set_piece(index, piece)

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
                color = get_color(player)
                if check_check(color):
                    print(color, ' is in check')
                    if check_checkmate(color):
                        print(color, 'is in check mate')
                        print("The winner is: ", player)
                        exit()
                move = get_move(player)
                delta = get_delta(move)
                from_index = get_index(move[0])
                to_index = get_index(move[1])
                p = get_piece(from_index)
                if check_legal(move, color, delta, True) and not check_check(color):
                    move_piece(move)
                    if p in PIECE_NAMES["pawn"]:
                        if check_swap_pawn(to_index, color):
                            swap_pawn(to_index, color)
                    clear()
                    print_board()
                    break
                print(ERROR)

# Run -------------------------------------------------------------------------
main()
