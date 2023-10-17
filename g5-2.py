import numpy as np
import itertools

def solution(g):
    # Transpose because columns are smaller
    # matrix will be viewed as list of columns (not rows)
    g = np.array(g).T
    
    columnlen, rowlen = g.shape
    
    possible_columns = list(itertools.product([True,False], repeat=columnlen+1))
    
    solutioncount_previous_columns = {col:1 for col in possible_columns}

    for i in range(rowlen):
        
        solutioncount_current_columns = {}
        
        for column in possible_columns:
            
            for previous_column, previous_n in solutioncount_previous_columns.iteritems():
                
                if isColumnValid(column, previous_column, g[i]):
                    
                    new_n = previous_n
                    new_n += solutioncount_current_columns[column] if column in solutioncount_current_columns else 0
                    
                    solutioncount_current_columns[column] = new_n
                    
        solutioncount_previous_columns = solutioncount_current_columns
        
    return sum(solutioncount_previous_columns.values())
                
    
def isColumnValid(generatedPostColumn, previousPastColumn, currentColumn):
    for i in range(len(currentColumn)):
        
        boxSum = sum(generatedPostColumn[i:i+2]+previousPastColumn[i:i+2])
        
        if (boxSum == 1) != currentColumn[i]:
            return False
        
    return True

print(solution([[True,False,True],[False,True,False],[True,False,True]]))