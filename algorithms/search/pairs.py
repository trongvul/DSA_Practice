# Problem: Pairs
# Description: https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

def pairs(k, arr):
    count = 0
    S = set(arr)
    for val in arr:
        if val + k in S:
            count += 1        
    return count