import numpy as np
import itertools

def solution(g):
    # Transpose because columns are smaller
    # matrix will be viewed as list of columns (not rows)
    g = np.array(g).T
    
    rowlen = len(g)
    columnlen = len(g[0])
    
    possible_columns = itertools.product([True,False], repeat=columnlen+1)
    
    previous_columns = {col:1 for col in possible_columns}

    for i in range(rowlen):
        current_columns = {}
        for column in possible_columns:
            for previous_column, previous_n in previous_columns.iteritems():
                if isColumnValid(column, previous_column, g[i]):
                    new_n = previous_n
                    new_n += current_columns[column] if column in current_columns else 0
                    current_columns[column] = new_n
        
        previous_columns = current_columns
        
    return sum(previous_columns.values())
                
    
def isColumnValid(generatedPostColumn, previousPastColumn, currentColumn):
    for i in range(len(currentColumn)):
        x00 = previousPastColumn[i]
        x01 = previousPastColumn[i+1]
        x10 = generatedPostColumn[i]
        x11 = generatedPostColumn[i+1]
        
        if (sum([x00, x01, x10, x11]) == 1) != currentColumn[i]:
            return False
    return True

print(solution([[True,False,True],[False,True,False],[True,False,True]]))