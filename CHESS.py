import numpy as np
board = []
counter=0
wide = 1
for h in range (8):
    a=[]
    for w in range(6):
        if (h+w) % 2 == 0:
            a.append(1)
        else:
            a.append(0)
    board.append(a)
board = np.array(board)
print(board)
for h in range (8):
    for w in range (6):
        if board[h,w] == 1:
            counter += 1
print(counter)
