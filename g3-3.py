from fractions import Fraction
import numpy as np
import math
"""pseudo code

get terminal_state_indecies

get terminal_state_probabilites: (nominator, denominator)

find kgv

adjust each -> nominator of terminal_state_probabilites to kgv

return [...nominators, kgv]

"""

matr = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

def solution(m):
    
    m = np.array(m)
    
    terminal_state_indecies = []
    
    for i, v in enumerate(m):
        if sum(v) == 0:
            terminal_state_indecies.append(i)
            
    probs = get_state_probabilities(m)
    
    terminal_state_probs = [probs[i] for i in terminal_state_indecies]
    
    return convert_to_common_denominator_format(terminal_state_probs)
    
def get_state_probabilities(m):
    
    mfrac = to_fraction_matrix(m)
    
    startvec = np.zeros(len(m))
    startvec[0] = 1
    
    probs = np.zeros(len(m))
    
    temp = np.copy(mfrac)
    
    iterations = 32 #the higher, the preciser
    
    for i in range(iterations):
        probs += np.dot(startvec.T, temp)
        temp = np.dot(temp, mfrac)
    
    return [Fraction(x).limit_denominator() for x in probs]
    
def to_fraction_matrix(m):
    mfrac = []

    for v in m:
        vsum = v.sum()
        if vsum == 0:
            mfrac.append([0]*len(m))
            continue
        mfrac.append(v/v.sum())
    
    return np.array(mfrac)
  
def convert_to_common_denominator_format(terminal_state_probs):
  
    common_denominator = math.lcm(*map(lambda x: x.denominator, terminal_state_probs))
    
    res = []
    
    for frac in terminal_state_probs:
        res.append(frac.numerator*common_denominator // frac.denominator)
    
    res.append(common_denominator)
    
    return list(map(int,res))
  
print(solution(matr))

# print(convert_to_common_denominator_format([Fraction(0, 1), Fraction(3, 14), Fraction(1, 7), Fraction(9, 14)]))