# This one works!!!! But its function is more limited to a 3 character word

def wordSearch(grid, word):
    width = len(grid[0])
    height = len(grid)
    total = 0
    
    for row in range(height): #0-n as a tracker for the LINES of the grid
        for col in range(width): #0-n as a tracker for the COLUMNS of the grid
            if (grid[row][col]=='A'):
                if (row-1 >= 0) and (col-1 >= 0) and (row+1 < height) and (col+1 < width):
                    if(grid[row-1][col-1]=='M') and (grid[row+1][col+1]=='S'): #top left to bottom right
                        if(grid[row-1][col+1]=='M') and (grid[row+1][col-1]=='S'): #top right to bottom left
                            total += 1
                        elif(grid[row-1][col+1]=='S') and (grid[row+1][col-1]=='M'): #flip word2
                            total += 1
                    elif(grid[row-1][col-1]=='S') and (grid[row+1][col+1]=='M'): #flip word1
                        if(grid[row-1][col+1]=='M') and (grid[row+1][col-1]=='S'): #top right to bottom left
                            total += 1
                        elif(grid[row-1][col+1]=='S') and (grid[row+1][col-1]=='M'): #flip word2
                            total += 1
    return total


# Read the grid from the input file
with open('day4\input.txt', 'r') as file:
    grid = [line.strip() for line in file]

word = 'MAS'
print(f"Total matches for X-MAS: {wordSearch(grid, word)}")
