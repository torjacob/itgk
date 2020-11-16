## a) Lag en funksjon som skriver ut brettet:
# For lettere skriving av brett
def convert_string_board(boardString = 9 * ' '):
    board_1d = list(boardString)
    board_2d = [board_1d[i:i+3] for i in range(0, len(board_1d), 3)]
    return board_2d

# Printing av brett
def print_board(board = convert_string_board()):
    # Forste linjer
    print('    1   2   3')
    line = '  ' + 13 * '-'
    print(line)

    # Ruter
    i = 0
    for row in board:
        formating = str('| ' + ' | '.join(row) + ' |')
        print(i + 1, formating)
        print(line)
        i += 1

## b) Lag en funksjon som sjekker om en spiller har vunnet:
def check_winner(board):
    a = ''
    result = None

    # Hjelpefunksjon for aa sjekke vinner:
    def check_trip(trip):
        if trip == 'xxx':
            return True
        elif trip == 'ooo':
            return False

    # Sjkker retnigner
    for row in board: # horisontal
        rowtrip = a.join(row)
        result = check_trip(rowtrip)
        if result != None:
            return result

    for i in range(3): # vertikal
        coltrip = ''
        for j in range(3):
            coltrip += board[j][i]
        result = check_trip(coltrip)
        if result != None:
            return result

    diatrip = ''
    for i in range(3): # diagonal \
        diatrip += board[i][i]
    result = check_trip(diatrip)
    if result != None:
        return result

    i = 2
    diatrip = ''
    for j in range(3): # diagonal /
        diatrip += board[i][j]
        i -= 1
    result = check_trip(diatrip)
    if result != None:
        return result

## c) Lag en funksjon som tar inn navnene til de to brukerne.
def get_player_names():
    player1 = str(input("Enter the name of player 1: "))
    player2 = str(input("Enter the name of player 2: "))
    return [player1, player2]

## d) Lag en funksjon som sjekker om et trekk er lovlig, altså at det ikke finnes andre brikker der.
def check_legal(pos, board):
    try:
        x = int(pos[0]) - 1
        y = int(pos[1]) - 1
        if board[y][x] == ' ':
            return True
        else:
            print('Stop, you violated the law! Pay the court a fine, or serve your sentence.')
            return False
    except:
        print('That\'s not a spot on the board.')
        return False

## e) Lag en funksjon som sjekker at input fra brukeren er riktig, altså at man ikke skriver inn rare tegn, eller skriver inn koordinater utenfor spillebrettet.
def check_valid(pos, board):
    for p in pos:
        p = str(p)

    if ( # Delt opp for oversiktlighet
        pos[0].isnumeric() == False or
        pos[1].isnumeric() == False or
        1 > int(pos[1]) > len(board[0]) or
        1 > int(pos[0]) > len(board)
    ):
        print('That\'s not a valid move.')
        return False
    else:
        return True

## f) Sett dette sammen til et fullverdig 3 på rad spill!
from os import system, name

# Tommer skjerm
def clear():
    if name == 'nt': # windows
        _ = system('cls')
    else:  # unix (posix)
        _ = system('clear')

# Faar moves fra player
def fetch_move(player):
    pos = input(player + ", enter the placement of your piece: ('x y')")
    return pos.split()

# Plasserer brikke
def place_piece(piece, move, board):
    new_board = board
    new_board[int(move[1]) - 1][int(move[0]) - 1] = piece
    return new_board

def main():
    # SETUP
    players = get_player_names()
    board = convert_string_board(9 * ' ')
    clear()
    print_board()

    # MAIN GAME LOOP
    while True:
        for player in players: # setter brikke basert pa hvilken spillers tur
            if players.index(player) == 0:
                piece = 'x'
            else:
                piece = 'o'

            while True: # tar inn move, sjekker om valid - plasserer
                move = fetch_move(player)
                if check_legal(move, board) and check_valid(move, board):
                    board = place_piece(piece, move, board)
                    clear()
                    print_board(board)
                    break

            # Sjekker vinner
            if check_winner(board) == True: # X har vunnet
                print('Congrats, ' + players[0] + ' you Won!')
                quit()
            elif check_winner(board) == False: # Y har vunnet
                print('Congrats, ' + players[0] + ' you Won!')
                quit()

main()
