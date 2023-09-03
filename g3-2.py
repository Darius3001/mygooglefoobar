def solution(n):
    res = 0
    
    for count_own_deck in reversed(range(1,n)): 
        res += recsolution(n-count_own_deck, count_own_deck)
        
    return res

dmap = {}

def recsolution(n, prev):
    if n in dmap.keys():
        return dmap[n]
        
    res = 1
    
    for count_own_deck in reversed(range(1,min(n,prev-1))): 
        print(count_own_deck)
        res += recsolution(n-count_own_deck, count_own_deck)
        
    dmap[n] = res
    
    return res
print(solution(4))
print(dmap)