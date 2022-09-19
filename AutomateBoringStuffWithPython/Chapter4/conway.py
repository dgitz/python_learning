# Conway's Game of Life
import time,random,copy,sys

WIDTH=60
HEIGHT = 20

STARTCELLS = 200
nextCells = []

for x in range(WIDTH):
   column = []
   for y in range(HEIGHT):
        column.append(' ')
   nextCells.append(column)

for i in range(STARTCELLS):
    x = random.randint(0,WIDTH-1)
    y = random.randint(0,HEIGHT-1)
    nextCells[x][y] = '#'

#for x in range(WIDTH):
#    column = []
#    for y in range(HEIGHT):
#        if random.randint(0,1) == 0:
#            column.append('#')
#        else:
#            column.append(' ')
#    nextCells.append(column)

iterationCount = 0
while True:
    cellCount = 0
   
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='')
        print()
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
                cellCount += 1
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
                cellCount += 1
            else:
                nextCells[x][y] = ' '


    iterationCount += 1
    print('Pop: ' + str(cellCount)  + ' Generation: ' + str(iterationCount))
    if cellCount == 0:
        print('Your world is Dead.  Ending.')
        sys.exit()
            
    time.sleep(.1)