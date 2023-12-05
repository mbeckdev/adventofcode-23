import os
puzzleNo = "2"
partNo = "1"

testPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "test", partNo, ".txt"]
testPath = "".join(testPathStringsList)
realPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "input", partNo, ".txt"]
realPath = "".join(realPathStringsList)
print(testPath)

print('********** start ********** start *******')
# which games are possible with these:
# only 12 red cubes, 13 green cubes, and 14 blue cubes
actualRed = 12
actualGreen = 13
actualBlue = 14

class MyClass:
    def __init__(self, parameter1, parameter2):
        # This is the constructor method, called when an object is created
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    def my_method(self):
        # This is a method of the class
        print(f"My method called with parameters: {self.parameter1}, {self.parameter2}")

# Creating an instance of the class
my_instance = MyClass("value1", "value2")

# Accessing attributes and calling methods of the instance
print(my_instance.parameter1)
print(my_instance.parameter2)
my_instance.my_method()

class Game:
    def __init__(self, setA, setB, setC) -> None:
        self.setA = setA
        self.setB = setB
        self.setC = setC
class BlockSet:
    def __init__(self, redblocks=0, greenblocks=0, blueblocks=0):
        self.redblocks = redblocks
        self.greenblocks = greenblocks
        self.blueblocks = blueblocks
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
print('{block_setA.display_blocks}')
print(block_setA.display_blocks())
print(block_setA.redblocks)
print('bbbbbdfasdfasdfasdf')
gameA = Game(block_setA, block_setB, block_setC)
print(gameA.setA.redblocks)

with open(testPath, "r") as file:
# with open(realPath, "r") as file:
    lines = file.readlines()
    print(lines)
    ans = 0
    for rawline in lines:
        line = rawline.strip()
        print(line)   # line is like 1abc2df
    #     # print(line.strip())    # the strip gets rid of spaces and crlf 's  line is ilke 3sfd1fj
        
        # game, set, color, number of color



    #     first = "empty"
    #     last = "empty"
    #     for char in line:
    #         if char.isdigit() and first == "empty":
    #             first = char
    #             # print(char)
    #         if char.isdigit():
    #             last = char
    #             # print(char)
    #     num = int(first + last)
    #     # print("num = ")
    #     # print(num)
    #     ans += num
    #     # print(line.find([0-9]))
print('***********end**********end*******')
print(ans)

