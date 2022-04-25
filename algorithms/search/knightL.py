# Problem: KnightL on a Chessboard
# Description: https://www.hackerrank.com/challenges/knightl-on-chessboard/problem
from collections import deque

def knightlOnAChessboard(n):
    result = [[0]*(n-1) for _ in range(n-1)]
    for i in range(1, n):
        for j in range(i, n):
            moves = get_moves(i,j,n)
            result[i-1][j-1] = moves
            result[j-1][i-1] = moves
    return result  

def get_moves(a,b,n):
    direction = [[a, b], [-a, b], [a, -b], [-a, -b],
    [b, a], [-b, a], [b, -a], [-b, -a]]
    visited = [[False]*(n) for _ in range(n)]
    # x,y,depth
    L = deque([(0, 0, 0)])
    visited[0][0] = True
    while L:
        x, y, l = L.popleft()
        for dx, dy in direction:
            new_x = x + dx
            new_y = y + dy
            new_l = l + 1
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                if new_x == n-1 and new_y == n-1:
                    return new_l
                
                L.append((new_x, new_y, new_l)) 
                
                visited[new_x][new_y] = True
    return -1
    
