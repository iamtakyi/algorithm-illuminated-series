from math import sqrt

def euclidean(p1, p2):
    return sqrt(pow(abs(p1[0] - p2[0]), 2) + pow(abs(p1[1] - p2[1]), 2))

def closestSplitPair(sy, best, delta):
    if len(sy) > 1:
        for i in range(len(sy)):
            for j in range(i + 1, min(7, len(sy) - i)):
                dist = euclidean(sy[i], sy[j])
                if dist < delta:
                    delta = dist
                    best = (sy[i], sy[j])
    return best, delta 

def closestPair(px, py):
    if len(px) <= 3:
        delta = float('inf')
        best = (None, None)
        #bruteforce if the length comes to 2 or 3
        for i in range(len(px) - 1):
            for j in range(i+1, len(px)):
                dist = euclidean(px[i], px[j])
                if dist < delta:
                    delta = dist
                    best = (px[i], px[j])
        return best, delta

    lpx = px[0 : (len(px)//2)]
    rpx = px[(len(px)//2) : ]
    lpy = [x for x in py if x in lpx]
    rpy = [x for x in py if x in rpx] #the composition runs in qdtrc time
    l, ld = closestPair(lpx,lpy)
    r, rd = closestPair(rpx,rpy)
    best, delta = (l, ld) if ld < rd else (r, rd)
    median = lpx[-1][0]
    sy = [x for x in py if x[0] >= (median - delta) and x[0] <= (median + delta)] #  [x for x in py if x[0] >= median[0] - delta and x[0] <= median[0] + delta]
    s, sd = closestSplitPair(sy, best, delta)
    return (best, delta) if delta < sd else (s, sd) 
    
def closestClosest(arr, func=closestPair):
    px = sorted(arr, key=lambda k:k[0])
    py = sorted(arr, key=lambda k:k[1])
    best,delta = func(px,py)
    return best, delta
    

lst4 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

print(closestClosest(lst4))