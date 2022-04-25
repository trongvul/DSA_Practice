# Problem: Ice Cream Parlor
# Description: https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true

def icecreamParlor(m, arr):
    data = {}
    for i, value in enumerate(arr):
        if (m - value) in data:
            return data[m - value] + 1, i + 1
        else:
            data[value] = i
