def solution(n):
    res = 0
    for i in range(1,n):
        res += recsolution(n-i, minimum=i+1)
    return res

dmap = {}

def recsolution(n, minimum=1):
    if n<minimum:
        return 0
        
    if n in dmap:
        return dmap[n]
        
    res = 1
    for i in range(minimum,n):
        res += recsolution(n-i, minimum=i+1)
    dmap[n] = res
    return res
  
x=solution(200)
print(x)

