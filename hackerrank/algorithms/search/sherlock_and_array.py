# Problem: Sherlock and Array
# Description: https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

def balancedSums(arr):
    right = sum(arr)
    left = 0
    for value in arr:
        right -= value
        if right == left:
            return 'YES'
        left += value
            
    return 'NO'