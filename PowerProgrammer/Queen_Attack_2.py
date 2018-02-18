#!/bin/python3
from collections import defaultdict
import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
rQueen, cQueen = input().strip().split(' ')
rQueen, cQueen = [int(rQueen), int(cQueen)]
chess_board = [[[0, False] for i in range(n)] for j in range(n)]
cb = defaultdict(lambda : [])

for a0 in range(k):
    rObstacle, cObstacle = input().strip().split(' ')
    rObstacle, cObstacle = [int(rObstacle), int(cObstacle)]
    # your code goes here
    chess_board[rObstacle-1][cObstacle-1][1] = True

i, j = rQueen-1, cQueen-1
count = 0

while i >= 0:
    if i-1 >= 0:
        if chess_board[i-1][j][1] is False:
            count += 1
        else:
            break
    i -= 1

i, j = rQueen-1, cQueen-1

while i < n:

    if i+1 < n:
        if chess_board[i+1][j][1] is False:
            count += 1
        else:
            break
    i += 1

i, j = rQueen-1, cQueen-1

while j >= 0:
    if j-1 >= 0:
        if chess_board[i][j-1][1] is False:
            count += 1
        else:
            break
    j -= 1

i, j = rQueen-1, cQueen-1

while j < n:

    if j+1 < n:
        if chess_board[i][j+1][1] is False:
            count += 1
        else:
            break
    j += 1


i, j = rQueen-1, cQueen-1

while i >= 0 and j >= 0:
    if i-1 >= 0 and j-1 >= 0:
        if chess_board[i-1][j-1][1] is False:
            count += 1
        else:
            break
    i -= 1
    j -= 1

i, j = rQueen-1, cQueen-1

while i < n and j >= 0:
    if i+1 < n and j-1 >= 0:
        if chess_board[i+1][j-1][1] is False:
            count += 1
        else:
            break
    i += 1
    j -= 1

i, j = rQueen-1, cQueen-1

while i < n and j < n:
    if i+1 < n and j+1 < n:
        if chess_board[i+1][j+1][1] is False:
            count += 1
        else:
            break
    i += 1
    j += 1

i, j = rQueen-1, cQueen-1

while i >= 0 and j < n:
    if i-1 >= 0 and j+1 < n:
        if chess_board[i+1][j+1][1] is False:
            count += 1
        else:
            break
    i -= 1
    j += 1


print(count)
