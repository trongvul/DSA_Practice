# Problem: Gridland Metro
# Description: https://www.hackerrank.com/challenges/gridland-metro/problem?isFullScreen=true

def gridlandMetro(n, m, k, track):
    d = {}
    total = n*m
    # number of cells that makes up train tracks
    count = 0
    for row, start, end in track:
        # the row is recognized for the first time
        if row not in d:
            d[row] = end
            count += end - start + 1
        else:
            last_end = d[row]
            # the current track does not overlap with the previous on
            if last_end < start:
                count += end - start + 1
                d[row] = end
            # the current track overlaps with the previous on
            elif last_end < end:
                count += end - last_end 
                d[row] = end
    return total - count       

