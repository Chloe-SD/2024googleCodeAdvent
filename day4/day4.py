
def wordSearch(grid, word):
    #print(grid)
    width = len(grid[1])
    height = len(grid)
    print(f"width: {width}\nheigh: {height}")
    #print(grid[4][3]) #access a single char
    total = 0

    def traverse(row,col,dx,dy):
        for i in range(len(word)):
            x,y = row+i*dx, col+i*dy
            if x<0 or y<0 or x>=height or y>=width or grid[x][y] != word[i]:
                # 4 checks for out of range. one check to see if the letter at this location is correct
                return False
        return True


    for row in range(height): #0-n as a tracker for the LINES of the grid
        for col in range(width): #0-n as a tracker for the COLUMNS of the grid
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals
            for dx, dy in directions:
                if traverse(row, col, dx, dy):
                    total +=1
    return(total)
            

        







with open('day4\input.txt', 'r') as file:
    grid = [line.strip() for line in file]
word = 'XMAS'
print(f"Toal matches for the word - {word}: {wordSearch(grid, word)}") 
