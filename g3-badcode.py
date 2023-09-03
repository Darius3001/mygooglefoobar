s=0
# took to long in runtime (O(2^n))
def solution(n):
  global s
  s+=1
  print(f'{"-"*(s-1)}{n}')
  n=int(n)
  res = 0
  while n != 1:
      if n%2==0:
          n>>=1
          print(f'{"-"*(s-1)}{n}')
          res+=1
      else:
          res+=1
          print(f'{"-"*s}plus')
          plus = solution(n+1)
          print(f'{"-"*s}minus')
          minus = solution(n-1)
          s-=1
          return res + min(plus, minus)
  s-=1
  return res
  
print(solution(15))