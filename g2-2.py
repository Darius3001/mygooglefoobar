def solution(n, b):
    
    path = []
    
    z = n
    k = len(n)
    
    while z not in path:
        path.append(z)
        z = step(z, b, k)
        
    index = path.index(z)
    
    return len(path)-index
        
def step(z, b, k):
    x = list(z)
    y = list(z)
    
    x = list(map(int, x))
    y = list(map(int, y))
    
    x.sort(reverse=True)
    y.sort()
    
    x = get_int_from_base(x,b)
    y = get_int_from_base(y,b)
    
    res = x-y
    
    return to_str_with_base(res, b, k)
    
def get_int_from_base(x, b):
    res = 0
    for index, it in enumerate(reversed(x)):
        res += it*(b**index)
        
    return res
    
def to_str_with_base(x, b, k):
    res = []
    
    i=0
    while x != 0:
        res.append(x%b)
        x=int(x/b)
        i+=1
    res.reverse()
     
    resstr = ''.join(list(map(str, res)))
    
    mz = k-len(resstr)
    
    resstr = ("0"*mz)+resstr
    
    return resstr
  
x = solution('1211', 10)
print(x)