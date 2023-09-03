def solution(n):
    n=int(n)
    res = 0
    while n > 1:
       res+=1
       if n%2==0:
           n>>=1
       elif (n>>1)%2==0 or n == 3:
           n-=1
       else:
           n+=1
           
    return res

print(solution(3))