
def wordSearch(grid, word):
   return 1


word = 'XMAS'
with open('day4\\test.txt', 'r') as file:
    grid = [line.strip() for line in file]

word = 'XMAS'
match_count = wordSearch(grid, word)
print(f"Number of matches for the word '{word}': {match_count}")