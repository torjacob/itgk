def make_board(string):
    index = 0
    brd = []
    for i in range(5):
        row = []
        for j in range(5):
            if string[index] == ".":
                row.append(None)
            else:
                row.append(string[index])
            index += 1
        brd.append(row)
    return brd

def get_piece(board, x, y):
    calX = 5 - x
    calY = 5 - y

    return board[calY][calX]

def get_legal_moves(board, x, y):
    piece = get_piece(board, x, y)

    legal_moves_list = []

    if piece.lower() == "p":
        iece.lowe
    else:
        legal_moves_list.append(None)

    return legal_moves_list



board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
board = make_board(board_string_1)

print(board)
print(get_piece(board, 2, 1))
print(get_piece(board, 5, 2))
