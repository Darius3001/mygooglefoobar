from itertools import combinations

def solution(num_buns, num_required):
  key_copies = num_buns - num_required + 1
  
  res = [[] for _ in range(num_buns)]
  
  c = combinations(range(num_buns), key_copies)
  
  for key, positions in enumerate(c):
    for pos in positions:
      res[pos].append(key)
    
  return res

print(solution(4,3))