import numpy as np
import itertools

def solution(g):
    # Transpose because columns are smaller
    # matrix will be viewed as list of columns (not rows)
    g = np.array(g).T
    
    columnlen, rowlen = g.shape
    
    possible_columns = list(itertools.product([True,False], repeat=columnlen+1))
    
    solutioncount_columns = {col:1 for col in possible_columns}

    for i in range(rowlen):
        solutioncount_columns = nextColumnSolutionCount(
            solutioncount_columns,
            g[i],
            possible_columns
        )
        
    return sum(solutioncount_columns.values())

def nextColumnSolutionCount(solutioncount_previous_columns, currentColumn, possible_columns):
    
    result = {}
    
    for column in possible_columns:
        
        for previous_column, previous_n in solutioncount_previous_columns.iteritems():
            
            if isColumnValid(column, previous_column, currentColumn):
                
                new_n = previous_n
                new_n += result[column] \
                    if column in result else 0
                
                result[column] = new_n
                
    return result

def isColumnValid(generatedPastColumn, previousPastColumn, currentColumn):
    
    for i in range(len(currentColumn)):
        
        boxSum = sum(generatedPastColumn[i:i+2]+previousPastColumn[i:i+2])
        
        if (boxSum == 1) != currentColumn[i]:
            return False
        
    return True

print(solution([[True,False,True],[False,True,False],[True,False,True]]))