# Problem: Missing Numbers
# Description: https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true

def missingNumbers(arr, brr):
    d = {}
    
    for value in arr:
        if value not in d:
            d[value] = -1
        else:
            d[value] -= 1
    
    for value in brr:
        if value not in d:
            d[value] = 1
        else:
            d[value] += 1
    
    result = []
    for i in d:
        if d[i] > 0:
            result.append(i)
    
    return sorted(result)
