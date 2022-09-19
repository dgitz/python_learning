import pdb
def buildSpaces():
    validSpaces = []
    for i in range(0,8):
        for j in range(0,8):
            validSpaces.append(str(i+1) + chr(97+j) )
    return validSpaces
def isValidChessBoard(board):
    isValid = False
    whiteCount = 0
    blackCount = 0
    whitePawnCount = 0
    blackPawnCount = 0
    for piece in board.values():
        if len(piece) == 0: 
            return False
        if piece[0] == 'w':
            whiteCount += 1
            if piece[1:] == 'pawn':
                whitePawnCount += 1
        elif piece[0] == 'b':
            blackCount += 1
            if piece[1:] == 'pawn':
                blackPawnCount += 1
        else:
            return False
    if (whiteCount > 16) or (blackCount > 16):
        return False
    if (whitePawnCount > 8) or (blackPawnCount > 8):
        return False
    # Piece Checks
    if ('bking' in board.values()) and ('wking' in board.values()):
        isValid = True
    
    # Space Checks
    validSpaces = buildSpaces()
    for space in board.keys():
        if space in validSpaces == False:
            return False
    return isValid

Boards = []
Boards.append({'valid':True,'board': {'1h': 'bking', '6c': 'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}})
Boards.append({'valid':False,'board': {'1h': '', '6c': 'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'}})
Boards.append({'valid':False,'board': {'1h': 'bking', '6c': 'wqueen','2g':'bbishop','5h':'bqueen','3e':''}})
Boards.append({'valid':True,'board': {'1a': 'wpawn', '1b': 'wpawn','2g':'wpawn','5h':'wpawn','3e':'wpawn','4d':'wpawn','5d':'wpawn','6a':'wpawn','1d':'wking','1e':'bking'}})
Boards.append({'valid':False,'board': {'1a': 'bpawn', '1b': 'bpawn','2g':'bpawn','5h':'bpawn','3e':'bpawn','4d':'bpawn','5d':'bpawn','6a':'bpawn','2d':'bpawn'}})
Boards.append({'valid':False,'board': {'1q': 'bpawn', '1b': 'bpawn','2g':'bpawn','5h':'bpawn','3e':'bpawn','4d':'bpawn','5d':'bpawn','6a':'bpawn','2d':'bpawn'}})
allGood = True
for i in range(len(Boards)):
    expectedValue = Boards[i]['valid']
    board = Boards[i]['board']
    isValid = isValidChessBoard(board)
    if isValid != expectedValue:
        print('Board: ' + str(i) + ' FAILED!')
        allGood = False

if allGood == True:
    print('All Tests Passed!')

    