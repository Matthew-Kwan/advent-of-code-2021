"""
Advent of Code 2021
Problem 1: Sonar Sweep

Input: List of Integers - depths
Output: Integer - Number of positive increases in depth
"""

# Part 1
def sonarSweep() -> int:
    """
    Returns the number of positive depth increases

    Returns:
        num_measurements: number of positive measurement differences
    """

    # Load in the depths into list
    with open("./inputs/prob1.txt") as fh:
        depths = [int(x.strip()) for x in fh.readlines()]
    
    # iterate through depths
    num_measurements = 0
    for i in range(1,len(depths)):
        if depths[i] > depths[i-1]:
            num_measurements += 1
        
    return num_measurements
        

# Test run
ans = sonarSweep()
print(ans)

# Part 2
def sonarSweep2() -> int:
    """
    Returns the number of positive depth increases

    Returns:
        num_measurements: number of positive measurement differences
    """

    # Load in the depths into list
    with open("./inputs/prob1.txt") as fh:
        depths = [int(x.strip()) for x in fh.readlines()]
    
    # if depths less than 4
    if len(depths) < 4:
        return None
    
    # iterate through depths
    num_measurements = 0
    l = 1
    last_sum = sum(depths[0:3])
    for r in range(3,len(depths)):
        
        # get the sum of the current window
        window_sum = sum(depths[l:r+1])
        
        # if sum of current window bigger than the last
        if window_sum > last_sum:
            num_measurements += 1
        
        # reassign last_sum to window sum
        last_sum = window_sum

        # increment the left point of the window
        l += 1
        
    return num_measurements

ans2 = sonarSweep2()
print(ans2)
