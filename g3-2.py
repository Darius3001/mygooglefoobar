def solution(n):
    dpmap = {}
    
    def count_bricks_rec(total_bricks, prev_bricks):
        
        if total_bricks > n:
            return 0
        
        if total_bricks == n and prev_bricks > 0:
            return 1
            
        if (total_bricks, prev_bricks) in dpmap:
            return dpmap[(total_bricks, prev_bricks)]
        res = 0
        
        for n_curr_col in range(prev_bricks+1, n+1):
            res += count_bricks_rec(total_bricks + n_curr_col, n_curr_col)
        
        dpmap[(total_bricks, prev_bricks)] = res
        
        return res
    return count_bricks_rec(0,0)
  
print(solution(3))