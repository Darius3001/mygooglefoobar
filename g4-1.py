import copy

"""
if negative loop:
  return all bunnies
  
floyd alg

test all combinations (with order)
  
return max bunnies

  
"""

def solution(times, times_limit):
  num_bunnies = len(times)-2
  bunny_list = list(range(num_bunnies))
  
  fwm = create_floyd_warshall_matrix(times)
  
  if has_negative_loop(fwm):
    return bunny_list
  
  def get_max_bunny_path(current_cost = 0, traversed_bunnies=[]):
    
    past_index = 0 if traversed_bunnies == [] \
      else 1 + traversed_bunnies[len(traversed_bunnies)-1]
    
    if fwm[past_index][len(times)-1]+current_cost>times_limit:
      return []
    
    if set(traversed_bunnies) == set(bunny_list):
      return bunny_list
    
    maxBunnies = traversed_bunnies
    
    for bunny in set(bunny_list)-set(traversed_bunnies):
      next_traversed = traversed_bunnies[:]
      next_traversed.append(bunny)
      
      traverse_cost = fwm[past_index][bunny+1]
      
      recPath = get_max_bunny_path(current_cost+traverse_cost, next_traversed)
      
      if len(recPath) > len(maxBunnies):
        maxBunnies = recPath
      
    return sorted(maxBunnies)
  
  return get_max_bunny_path()

def create_floyd_warshall_matrix(m):
  res = copy.deepcopy(m)
  lenm = len(m)
  for k in range(lenm):
    for i in range(lenm):
      for j in range(lenm):
        res[i][j] = min(res[i][j],res[i][k]+res[k][j])
        
  return res

def has_negative_loop(fwm):
  for i in range(len(fwm)):
    if fwm[i][i] < 0:
      return True
    
  return False

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
