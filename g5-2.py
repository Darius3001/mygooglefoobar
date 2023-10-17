import numpy as np
import itertools

def solution(g):
    # Transpose because columns are smaller
    # matrix will be viewed as list of columns (not rows)
    g = np.array(g).T
    
    rowlen = len(g)
    columnlen = len(g[0])
    
    possible_columns = itertools.product([True,False], repeat=columnlen+1)
    
    
def isRowValid(generatedPostRow, previousPastRow, currentRow):
    for i in range(len(currentRow)):
        x00 = previousPastRow[i]
        x01 = previousPastRow[i+1]
        x10 = generatedPostRow[i]
        x11 = generatedPostRow[i+1]
        
        if (sum([x00, x01, x10, x11]) == 1) != currentRow[i]:
            return False
    return True

solution([[True,False,True],[False,True,False],[True,False,True]])