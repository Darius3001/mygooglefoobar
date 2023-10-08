from decimal import *
import decimal

decimal.getcontext().prec = 200

SQRT2 = decimal.Decimal(2).sqrt()

def solution(s):
  return str(beatty(Decimal(s)))

def little_gauss(n):
  return n*(n+1)/2
  
def beatty(n):
  if n < 1:
    return 0
  
  n1 = Decimal(n * (SQRT2-1)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
  
  return n*n1 + little_gauss(n) - little_gauss(n1) - beatty(n1)