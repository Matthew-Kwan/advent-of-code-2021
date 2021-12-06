"""
Advent of Code 2021
Problem 2: Dive!
"""

# part 1 and 2 (removed depth changes from part 1)
def submarinePosition():
    """
    Returns the depth * the horizontal position of t
    """
    
    # Load in data
    with open("./inputs/prob2.txt") as fh:
        instructions = [x.strip() for x in fh]
        
    depth = 0
    x_pos = 0
    aim = 0
    for instruct in instructions:
        di, val = instruct.split()
        val = int(val)
        
        if di == 'forward':
            x_pos += val
            depth += (aim * val)
            
        elif di == 'up':
            aim -= val
            
        else:
            aim += val

    return depth * x_pos

# Test Cases: part 1
ans = submarinePosition()
print(ans)
    