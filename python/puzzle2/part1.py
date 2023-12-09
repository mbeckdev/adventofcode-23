import os
puzzleNo = "2"
partNo = "1"

testPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "test", partNo, ".txt"]
testPath = "".join(testPathStringsList)
realPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "part", partNo, "input.txt"]
realPath = "".join(realPathStringsList)
print(realPath)

print('********** start ********** start *******')
# which games are possible with these:
# only 12 red cubes, 13 green cubes, and 14 blue cubes
actualRed = 12
actualGreen = 13                            
actualBlue = 14

# class MyClass:
#     def __init__(self, parameter1, parameter2):
#         # This is the constructor method, called when an object is created
#         self.parameter1 = parameter1
#         self.parameter2 = parameter2

#     def my_method(self):
#         # This is a method of the class
#         print(f"My method called with parameters: {self.parameter1}, {self.parameter2}")

# # Creating an instance of the class
# my_instance = MyClass("value1", "value2")

# # Accessing attributes and calling methods of the instance
# # print(my_instance.parameter1)
# # print(my_instance.parameter2)
# my_instance.my_method()

class Game:
    def __init__(self, gameId, passesCheck, setArray) -> None:
        self.gameId = gameId
        self.setArray = setArray
        self.passesCheck = passesCheck
    def __str__(self) -> str:
        return f'game id = {self.gameId}, passesCheck = {self.passesCheck}, setArray = {self.setArray}'
    # def __init__(self, gameId, setA, setB, setC) -> None:
    #     self.gameId = gameId
    #     self.setA = setA
    #     self.setB = setB
    #     self.setC = setC
        
    # def addBlockSet(self, whichset):
        # self.  maybe game should be an array of block sets so i can append
class BlockSet:
    def __init__(self, redblocks=0, greenblocks=0, blueblocks=0):
        self.redblocks = redblocks
        self.greenblocks = greenblocks
        self.blueblocks = blueblocks
    def __str__(self):
        return f"BlockSet(red={self.redblocks}, green={self.greenblocks}, blue={self.blueblocks})"
    def __repr__(self):
       return f"BlockSet(red={self.redblocks}, green={self.greenblocks}, blue={self.blueblocks})"
    #    return f"BlockSet(id={self.id}, setArray={self.setArray})"
    def addblocks(self, red=0, green=0, blue=0):
        self.redblocks += red
        self.greenblocks +=green
        self.blueblocks +=blue
    def removeblocks(self, red=0, green=0, blue=0):
        self.redblocks = max(0, self.redblocks - red)
        self.greenblocks = max(0, self.greenblocks - green)
        self.blueblocks = max(0, self.blueblocks - blue)
    def display_blocks(self):
        print(f"Red Blocks: {self.redblocks}")
        print(f"Green Blocks: {self.greenblocks}")
        print(f"Blue Blocks: {self.blueblocks}")

block_setA = BlockSet(redblocks=5, greenblocks=3, blueblocks=7)
block_setB = BlockSet(redblocks=5, greenblocks=3, blueblocks=7)
block_setC = BlockSet(redblocks=5, greenblocks=3, blueblocks=7)
# print('{block_setA.display_blocks}')
# print(block_setA.display_blocks())
# print(block_setA.redblocks)
# print('bbbbbdfasdfasdfasdf')
# gameA = Game(block_setA, block_setB, block_setC)
# print(gameA.setA.redblocks)


checkSet = BlockSet(redblocks=12, greenblocks=13, blueblocks=14)
# print('checkSet.blueblocks',checkSet.blueblocks)
# checkSet.removeblocks(100,100,100)
# print('checkSet.blueblocks',checkSet.blueblocks)


# with open(testPath, "r") as file:
with open(realPath, "r") as file:
    lines = file.readlines()
    # print(lines)

    allGames = []
    for rawline in lines:
        line = rawline.strip()
        # print(line)   # line is like 1abc2df
    #     # print(line.strip())    # the strip gets rid of spaces and crlf 's  line is ilke 3sfd1fj
        
        # game, set, color, number of color
        lineA = line.split(':')
        gamestring=lineA[0]
        setsstring=lineA[1]
        gameNo = int(gamestring.split(' ')[-1])
        # print('gameno = ', gameNo)
        # print('setsst/ring = ', setsstring)

        sets = setsstring.split(';')
        thisGameArray = []
        thisGamePassesCheck = True
        for set in sets:
            blah = set.strip()
            # print('set = ',set)
            numandcolors = set.strip().split(',')

            numred = 0
            numgreen = 0
            numblue = 0
            for numandcolorstr in numandcolors:
                numandcolor = numandcolorstr.strip().split(' ')
                num = int(numandcolor[0])
                color = numandcolor[1]
                if color == 'red': numred = num
                if color == 'green': numgreen = num
                if color == 'blue': numblue = num
            
            blockset7 = BlockSet(numred,numgreen,numblue)
            # blockset7.display_blocks()
            # print(blockset7)
            thisGameArray.append(blockset7)

            #check if this set agains checkSet
            if ((blockset7.redblocks > checkSet.redblocks) or (blockset7.blueblocks > checkSet.blueblocks) or (blockset7.greenblocks > checkSet.greenblocks)) :
                # print(f'AHA - game {gameNo} and set with {blockset7}')
                # if mygame is higher number than check, then it's a bad game
                thisGamePassesCheck = False

 
        # print('sets = ',sets)
        newGame = Game(gameNo, thisGamePassesCheck, thisGameArray)
        allGames.append(newGame)
        # print('thisGame = ',newGame)

print('***********end**********end*******')
# print all games - for checking 
# for index, game in enumerate(allGames):
#    print(f"{game}")

# add up the ids of all the possible games
ans = 0
for index, game in enumerate(allGames):
    # if (game.gameId): print(game.gameId)
    if (game.passesCheck): 
        ans += game.gameId
        # print(f'gameid {game.gameId} passesCheck') 
print(f'ans = {ans}')

