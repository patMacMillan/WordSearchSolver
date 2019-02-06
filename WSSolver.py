# Vars
word_search = [['t', 'h', 'g', 'i', 'r'],
               ['i', 'k', 'k', 't', 'j'],
               ['g', 'k', 'i', 't', 'e'],
               ['h', 'k', 'k', 'i', 'm'],
               ['t', 'a', 'e', 'm', 'e']]

word_bank = ['tim', 'kite', 'right', 'tight']

# Functions

# Searches for a specific word in a word search puzzle
# Takes in a word and a puzzle
#
# Returns the co-ordinates of the found word
def search(word, puzz):
    for letter in word:
        # Go letter by letter in the puzzle until you find the first letter of the word
        for x in range(len(puzz)):
            for y in range(len(puzz)):
                if letter == puzz[x][y]:
                    print('Found ' + letter + ' at ' + str(x) + ',' + str(y))
                    # Retreive co-ordinates
                    coords = getCO(x,y,word,puzz)
                    if not (coords == []):
                        return coords
# Gets Coordinates for the found word
# Takes in initial x and y value, the word that needs to be found, and the puzzle
#
# Returns a list of coordinates if the word was found, returns an empty list is not
def getCO(x, y, word, puzz):
    coords = []
    dirs = []
    movs = updateMovs(x,y)
    # Find direction
    dirs = findDir(movs,word[1],puzz)
    for dir in dirs:
        print(dir)
        # Reinit movs with initial values
        movs = updateMovs(x, y)
        coords = [[x, y]]
        # Iterate from the second letter to the end of the word.
        for letIndx in range(1, len(word), 1):
            currLet = word[letIndx]
            #print('On ' + word + ': looking for ' + word[letIndx])
            if inRange(movs[dir][0], movs[dir][1], len(puzz), len(puzz[0])):
                if puzz[movs[dir][0]][movs[dir][1]] == currLet:
                    print('Found ' + currLet + ' at ' + str(movs[dir][0]) + ',' + str(movs[dir][1]))
                    coords.append([movs[dir][0], movs[dir][1]])
                    movs = updateMovs(movs[dir][0], movs[dir][1])
                    # Finds if at last index
                    if letIndx == (len(word) - 1):
                        print('Found ' + word + '!')
                        return coords
                else:
                    coords = []
                    break
    print('Not here, restarting search for ' + word + '...')
    return []
# Tells if the item is range
# Takes in x, y, x upper lim, and y upper lim.
#
# Returns True or False. Mainly used for cleaner code.
def inRange(x, y, xUlim, yUlim):
    if (x >= 0) and (x < xUlim) and \
            (y >= 0) and (y < yUlim):
        return True
    else:
        return False
# Updates movement list
# Takes in current x and y value
#
# Returns the potential movements in all 8 directions
def updateMovs(x, y):
    # Valid movements
    movements = [[x, y - 1], [x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
                 [x, y + 1], [x + 1, y + 1], [x + 1, y], [x + 1, y - 1]]
    return movements
# Finds the direction in which a word could potetially be
# Takes the current movements, the second letter of a word, and the puzzle
#
# Returns a list of movement indexes that are in the potential direction of a possible word
def findDir(movs, lett, puzz):
    dirList = []
    xLim = len(puzz)
    yLim = len(puzz[0])
    for dir in range(len(movs)):
        # Make sure value is in range
        if (movs[dir][0] >= 0) and (movs[dir][0] < xLim) and \
           (movs[dir][1] >= 0) and (movs[dir][1] < yLim):
            # Current letter based on the direction movement.
            currLett = puzz[movs[dir][0]][movs[dir][1]]
            if currLett == lett:
                #print('Found match on index %d' % dir)
                dirList.append(dir)
    print(dirList)
    return dirList

def solve(words, puzz):
    ans_key = []
    for word in words:
        print('Searching word: ' + word)
        tmpList = search(word, puzz)
        #print(tmpList)
        listyboi = [word, tmpList]
        ans_key.append(listyboi)
    print('\n***********************************************')
    print('Word search solved: ')
    print(ans_key)

#print(getCO(0,4,word_bank[0],word_search))
#print(search(word_bank[0],word_search))
solve(word_bank, word_search)