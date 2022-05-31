# Problem: Minimum Loss
# Description: https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true

import sys

def minimumLoss(price):
    d = {}
    loss = sys.maxsize
    for i, p in enumerate(price):
        d[p] = i
    
    price = sorted(price)
    
    for i in range(len(price)-1):
        if d[price[i+1]] < d[price[i]]:
            loss = min(loss, price[i+1]- price[i])
    return loss  