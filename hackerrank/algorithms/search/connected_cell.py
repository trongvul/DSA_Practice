# Problem: Connected Cells in a Grid
# Description: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

def connectedCell(matrix):
    max_size = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                size = get_region_size(matrix, row, column)
                max_size = max(max_size, size)  
    return max_size

def get_region_size(matrix, row, column):
    if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[row]):
        return 0
    
    if matrix[row][column] == 0:
        return 0

    region_size = 1
    matrix[row][column] = 0
    for r in range(row-1, row+2):
        for c in range(column-1, column+2):
            if r != row or c != column:
                region_size += get_region_size(matrix, r, c)
    return region_size
