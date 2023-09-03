def solution(l):
    l.sort(reverse=True)
    n = list2num(l)
    
    if n % 3 == 0:
        return n
    
    mod1 = list(filter(lambda x: x%3==1, l))
    mod2 = list(filter(lambda x: x%3==2, l))
    mod1.sort()
    mod2.sort()
    
    if n%3==1:
        if len(mod1) > 0:
            l.remove(mod1[0])
        elif len(mod2) > 1:
            l.remove(mod2[0])
            l.remove(mod2[1])
        else:
            return 0
    else:
        if len(mod2) > 0:
            l.remove(mod2[0])
        elif len(mod1) > 1:
            l.remove(mod1[0])
            l.remove(mod1[1])
        else:
            return 0
    
    return list2num(l)
        
    
def list2num(x):
    return int(''.join(map(str, x)))
  
print(solution([3,1,4,1,5,9]))