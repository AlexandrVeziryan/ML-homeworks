def is_battleship(x, y):
    if board[x][y] == " ":
        return False
    if board[x][y] == ".":
        board[x][y] = " "
        return False
    else:
        board[x][y] = " "
        if x + 1 < lenn:
            is_battleship(x + 1, y)
        if y + 1 < lenn:
            is_battleship(x, y + 1)
        return True  

board = [["X",".",".","X"],[".",".",".","X"],["X","X",".","X"],[".",".",".","."]]
lenn = len(board)
original_board = []
for b, i in zip(board, range(lenn)): # Deep copy anel chstacvec
    original_board.append([])
    for j in b:
        original_board[i].append(j)
res = 0
for i in range(lenn):
    for j in range(lenn):
        if(is_battleship(i, j)):
            res += 1
print(board)        
print(original_board)        
print(res)        
