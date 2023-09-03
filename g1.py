def solution(s):
    
    longs = s+s
    
    for start in range(len(s)):
        for substrlen in range(1,len(s)):
            
            if len(s)%substrlen!=0:
                continue
            
            substr = longs[start:start+substrlen]
            
            print(substr)
            
            if isSubstringValid(substr, s):
                return substrlen
    return 1

def isSubstringValid(sub, s):
    
    longs = s+s
    
    for start in range(len(s)):
        
        solution = True
        
        for pos in range(start, len(s)+start, len(sub)):
            
            lsub = longs[pos:pos+len(sub)]
            
            if lsub != sub:
                solution = False
                break
            
        if solution:
            return True

r= solution('abccbaabccba')
print(r)