def solution(l):
    
    solution = maxrecursive(0, l)
    
    if solution == None:
        return 0
        
    return list2num(solution)
        

def maxrecursive(mod3, l):
    
    if len(l) == 1 and (l[0]+mod3)%3!=0:
        return None
    
    if len(l) == 1 and (l[0]+mod3)%3==0:
        return l
        
    maxSol = None
    
    for i in range(len(l)-1):
        
        item = l[i]
        sublist = l[i+1:]
        newmod3 = (mod3+item)%3
        
        subSolution = maxrecursive(newmod3, sublist)
        subSolutionWithoutItem = maxrecursive(mod3, sublist)
        
        if subSolution == None and subSolutionWithoutItem == None:
            continue
        
        if subSolution != None:
            subSolution.append(item)
        
        maxSub = getMax(subSolution, subSolutionWithoutItem)
        
        maxSol = getMax(maxSub, maxSol)
        
    return maxSol
        
        
def getMax(a,b):
    
    if a == None:
        return b
        
    if b == None:
        return a
    
    sortedA = a.copy()
    sortedA.sort(reverse=True)
    
    sortedB = b.copy()
    sortedB.sort(reverse=True)
    
    inta = list2num(sortedA)
    intb = list2num(sortedA)
    
    return sortedA if inta > intb else sortedB
    
def list2num(x):
    return int(''.join(map(str, x)))

for i in range(2,10):
    print(i)