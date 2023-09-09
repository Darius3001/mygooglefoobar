import copy

"""
if negative loop:
  return all bunnies
  
floyd alg

test all combinations (with order)
  
return max bunnies

  
"""

def solution(times, times_limit):
  numBunnies = len(times)-2
  # todo detect negative loops
  fwm = create_floyd_warshall_matrix(times)
  
  
  
  pass

def create_floyd_warshall_matrix(m):
  res = copy.deepcopy(m)
  lenm = len(m)
  for k in range(lenm):
    for i in range(lenm):
      for j in range(lenm):
        res[i][j] = min(res[i][j],res[i][k]+res[k][j])
        
  return res


print(create_floyd_warshall_matrix([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]))
    
