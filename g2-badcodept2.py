def solution(l):
    l.sort(reverse=True)
    return rec(0,l)
    
def rec(index, l):
    max = 0
    for i in range(index, len(l)):
        listWithItem = l.copy()
        listWithoutItem = l.copy()
        del listWithoutItem[i]
        
        lwi = rec(i+1, listWithItem)
        lwoi = rec(i, listWithoutItem)
        
        max = max(list2num(lwi), list2num(lwoi), max)
        
    return max
        
def list2num(x):
    return int(''.join(map(str, x)))
  
l = [1,2,1,2,4,2]
l.remove(2)
print(l)