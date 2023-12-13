import os
puzzleNo = "3"
partNo = "1"

# testPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "test", partNo, ".txt"]  # p2test1.txt
testPathStringsList = ["python\\puzzle", puzzleNo, "\\puz", puzzleNo, "test", partNo, ".txt"]
testPath = "".join(testPathStringsList)
realPathStringsList = ["python\\puzzle", puzzleNo, "\\puz", puzzleNo, "part", partNo, "input.txt"]
realPath = "".join(realPathStringsList)
print(realPath)
print(testPath)

print('********** start ********** start *******')
# hmm, have a x and y,  00 is at top left
# call this the gameboard.
# each cell:
#  checkall around this digit, see a mark, set a realPart = true, 
#      when finish a set of numbers, 
#           find the 3 digit or 5 digit or whatever, 
#           and reset the realPart to = false
#  capture the full number in an array of goodPartNums array
#  answer = add up all numbers in goodPartNums

# how does python with strings as arrays? guess I'll find out


# functions:
#   isThereASymbolAroundMe?(myX, myY) = returns true or false
#   isThereADigitToMyRight(myX, myY)? = returns true, will return false when you get to the end of a 'word' of digits

#   findWholeWord(myX, myY, wordLength)
#       I"m at teh end of a digit word, what's the whole digit word
#   addToGoodPartNums(newWord)    ? might be faster to just add it not in a function
#   findSumOfArray(myArray) 
# .....try no classes.... first   

def findSumOfArray(myArray):
    sum = 0
    for item in myArray:
        sum += item
    return sum
# testArray = ['20','3']  #no worky. so make sure things in array are numbers
testArray = [20,3]
# isdigit() True if all chas are digits 
def findWholeWord(myX, myY, gameboard):
    # we already know this is a digit
    thisCell = gameboard[myY][myX]
    wordLength = 1

    # is there one to the left? if so, check that one and increase some var
    if ((myX-1) >= 0):
        if (gameboard[myY][myX-1]):
            print(thisCell)

# class GameBoard:
#     def __init__(self, length, width) -> None:
#         self.width = width
#         self.length = length
#     # def __str__(self) -> str:
#         # for y in self.length:
#             # for x in self.width:
#                 # print()
#     def line
# class cell:
#     def __init__(self, x, y, digit) -> None:
#         this.x = x
#         this.y = y
#         this.digit = digit
        
        


with open(testPath, "r") as file:
# with open(realPath, "r") as file:
    boardWidth = 0
    boardLength = 0
    lines = file.readlines()
    # print(lines)

    # print(lines[0])
    # print(lines[1])
    # print(len(lines[0].strip()))

    boardtest = [[1,2],[5,6]]
    boardtest = [[12],[5,6]]
    maxX = 0
    maxY = 0
    # print(boardtest[1][0])  # 00 = 1, 01 = 2, 10 = 5, 11 = 6
    print('***((((()))))')
    # allGames = []
    board = [] #  board[y][x]    not x y
    for rawline in lines:
        line = rawline.strip()
        # print(line)   # line is like ..34$...f.
        lineArray = []
        for character in line:
            lineArray.append(character)
        # print(lineArray) # all strings in array
        board.append(lineArray)
    # print(board)
    # print(board[0][2])    # board y, x
    boardWidth = len(board[0])
    boardLength = len(board)
    maxX = boardWidth - 1
    maxY = boardLength - 1
    print(f'boardWidth = {boardWidth} and boardLength = {boardLength}')

    for yindex, yelement in enumerate(board):
    # for y in board:
        possibleWord = False
        endOfWord = False
        for xindex, cell in enumerate(board[yindex]):
            # cell = board[y][x]
            print(cell)   # starts top left and goes right first
            # check if this is a digit?
            isDigit = cell.isdigit()
            # print(isDigit)

            if (isDigit):
                possibleWord = True
                wordLength = 1
                # is there a digit to the right? if not, then go backwasrds
                if ((xindex + 1) <= boardWidth):
                    cellToRight = board[yindex][xindex + 1]
                    if (cellToRight.isdigit()):
                        # cell to right is a digit, so this cell is not end of word
                        endOfWord = False
                # is there a digit to the left? 
                howManycellsToCheck = xindex-1+1
                # for someIndex, element in enumerate(board[yindex]):
# hereeeeeeee
                # for i in range(xindex, 0, -1):
                #     if (i )

                #     if ((xindex - 1) >= 0):
                #         cellToLeft = board[yindex][xindex - 1]
                #         if (cellToLeft.isdigit()):
                #             wordLength += 1



  
# findWholeWord(2,0,2,board)
print('***********end**********end*******')
# print all games - for checking 
# for index, game in enumerate(allGames):
#    print(f"{game}")

# # add up the ids of all the possible games
# ans = 0
# for index, game in enumerate(allGames):
#     # if (game.gameId): print(game.gameId)
#     if (game.passesCheck): 
#         ans += game.gameId
#         # print(f'gameid {game.gameId} passesCheck') 
# print(f'ans = {ans}')

