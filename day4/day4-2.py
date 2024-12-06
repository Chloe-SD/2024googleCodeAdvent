
def wordSearch(grid, word):
    #print(grid)
    width = len(grid[1])
    height = len(grid)
    print(f"width: {width}\nheigh: {height}")
    #print(grid[4][3]) #access a single char
    total = 0

    def traverse(row,col,dx,dy):
        #print(f"from index {row}:{col}")
        for i in range(len(word)):
            x,y = row+i*dx, col+i*dy
            if x<0 or y<0 or x>=height or y>=width or grid[x][y] != word[i]:
                # 4 checks for out of range. one check to see if the letter at this location is correct
                return False
        return True


    for row in range(height): #0-n as a tracker for the LINES of the grid
        for col in range(width): #0-n as a tracker for the COLUMNS of the grid
            
            if traverse(row, col, 1, 1): # top left to bottom right
                #print(f"found 1 at {row}:{col}")
                if ((row+3 <= height) and (traverse(row+2, col, -1, 1))): #bottom left to top right
                    total+=1
                elif ((col+3 <= width) and (traverse(row, col+2, 1, -1))): #top right to bottom left
                    total+=1 
            elif traverse(row,col,-1,-1): #bottom right to top left
                #print(f"found 1 at {row}:{col}")   
                if ((row-2 >= 0) and (traverse(row-2, col, 1, -1))): #top right to bottom left
                    total+=1
                elif ((col-2 >= 0) and (traverse(row, col-2, -1, 1))): #bottom left to top right
                    total+=1 
                
                    
    return(total)
            


with open('day4\\test.txt', 'r') as file:
    grid = [line.strip() for line in file]
word = 'MAS'
print(f"Toal matches for x-word - {word}: {wordSearch(grid, word)}") 