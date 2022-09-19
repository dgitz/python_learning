import pdb
def printGrid(data):
    height = len(data)
    width = len(data[0])
    for x in range(0,height):
        for y in range(0,width):
            print(str(data[x][y]),end='')
        print()
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.']]
printGrid(grid)
