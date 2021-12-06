"""
Advent of Code 2021
Problem 3: Binary Diagnostic
"""
from collections import Counter
def binaryDiag():
    """
    Returns the diagnostics

    Returns:
        int: gamma times epsilon
    """
    
    with open('./inputs/prob3.txt') as fh:
        diags = [x.strip() for x in fh]
    
    positions = [Counter() for _ in range(len(diags[0]))]
    
    # Iterate through diags
    for i, diag in enumerate(diags):
        # iterate through binary and append to proper Counter
        for j in range(len(diag)):
            positions[j][diag[j]] = positions[j].get(diag[j], 0) + 1
    
    gamma = ""        
    epsilon = ""
    # Iterate through counters
    for counter in positions:
        most_common = counter.most_common()[0][0]
        gamma = gamma + most_common
        epsilon = epsilon + str(abs(int(most_common) - 1))

    # convert to dec
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    
    return gamma * epsilon

# Test Case
ans = binaryDiag()
print(ans)

#########################################################################
def binaryDiag2():
    
    with open('./inputs/prob3.txt') as fh:
        raw_diags = [x.strip() for x in fh]
    
    # For Oxy Rating
    diags = raw_diags
    positions = [Counter() for _ in range(len(diags[0]))]
    
    # Iterate through diags
    oxy_rating = ''
    for i in range(len(diags[0])):
        
        # if only 1 value left
        if len(set(diags)) == 1:
            oxy_rating = diags[0]
            break
        
        for j in range(len(diags)):
            positions[i][diags[j][i]] = positions[i].get(diags[j][i], 0) + 1
        
        ranks = positions[i].most_common()
        if ranks[0][1] == ranks[1][1]:
            rank_one = '1'
        else:
            rank_one = ranks[0][0]
        oxy_rating = oxy_rating + rank_one
        diags = [diag for diag in diags if diag.startswith(oxy_rating)]
    
    # For C02 scrubbing rating - need to find 2nd most popular index at every level
    diags = raw_diags
    positions = [Counter() for _ in range(len(diags[0]))]
    
    # Iterate through diags
    c02_rating = ''
    for i in range(len(diags[0])):
        
        # if only 1 value left
        if len(set(diags)) == 1:
            c02_rating = diags[0]
            break
        
        for j in range(len(diags)):
            positions[i][diags[j][i]] = positions[i].get(diags[j][i], 0) + 1
    
        ranks = positions[i].most_common()
        if ranks[0][1] == ranks[1][1]:
            rank_two = '0'
        else:
            rank_two = ranks[1][0]
        c02_rating = c02_rating + rank_two
        diags = [diag for diag in diags if diag.startswith(c02_rating)]
    
    # convert to decimal
    oxy_rating = int(oxy_rating, 2)
    c02_rating = int(c02_rating, 2)
     
    return oxy_rating * c02_rating

# Test Case
ans = binaryDiag2()
print(ans)