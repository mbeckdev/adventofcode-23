# ans = d55218
puzzleNo = "1"
partNo = "2"

testPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "test", partNo, ".txt"]
testPath = "".join(testPathStringsList)
realPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "input", partNo, ".txt"]
realPath = "".join(realPathStringsList)
print('testPath = ', testPath)
print('realPath = ', realPath)

print('********** start ********** start *******')


def getWordInThisString(someString, ):
    # print('kooool  someStrin = ', someString)
    for wordNumber in numsAsWords:
        if wordNumber in someString:
            # print(wordNumber,"looool")
            return wordNumber
    return "-1"
numsAsWords = ['zero','one','two','three','four','five','six','seven','eight','nine']
def getDigitFromWord(word):
    try:
        # Find the index of the word in the list and return the corresponding numerical value
        number = numsAsWords.index(word)
        return number
    except ValueError:
        # If the word is not in the list, return None or another suitable value
        return "word as a number is not in list"

# with open(testPath, "r") as file:
with open(realPath, "r") as file:
    lines = file.readlines()
    # print(lines)
    ans = 0
    # idea - check from left side - find a digit, or a name of a word (sixteen, vs six, = take only six )
    # numsAsWords = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for line in lines:
        # print(line)   # line is like 1abc2df
             # ahhh for got about this .. would have helped below # print(line.strip())    # the strip gets rid of spaces and crlf 's  line is ilke 3sfd1fj
        first = "empty"
        last = "empty"
        firstWord = ''
        lastWord = ''
        num = 0
        for char in line:
            if first == "empty":
                if char.isdigit():
                    first = char
                    # print("first is a digit and it is = ", first)
                if first == 'empty':
                    # check for a word number
                    firstWord += char
                    maybeWordInThisString = getWordInThisString(firstWord)
                    if maybeWordInThisString != "-1":
                        first = int(getDigitFromWord(maybeWordInThisString))
                    # print("first was a word and it is = ", first)
        # print ('aaaaaaaaaaaaaaa',str(line[::-1]))
        # print('e**************e line = ',line)
        reversedLine = ''.join(reversed(line))
        for char in reversedLine:
        # for char in reversed(line):
           
            # print("reversed char = ", char)
            if char and not char.isspace():
            # if char != '' and char != ' ':
                # print('char is real and is = ', char)
                if last == "empty":
                    # print('ddddddddddddddddddddddddddddddddddddddddddddddd, last = empty, char = ', char)
                    if char.isdigit():
                        last = char
                        # print("last is a digit and it is = ", last)
                    if last == 'empty':
                        # check for a word number
                        if lastWord != '':
                            lastWord = lastWord[::-1]
                        lastWord += char
                        lastWord = lastWord[::-1]
                        # print('lastWord = b=',lastWord)  
                        maybeWordInThisString = getWordInThisString(lastWord)
                        if maybeWordInThisString != "-1":
                            last = int(getDigitFromWord(maybeWordInThisString))
                            # print("last was a word and it is = ", last)
        
        # print("first = ", first)
        # print("last = ", last)
        num = str(first) + str(last)
        # num = int(first)
        # print("num = ", num)
        
        # print(num)
        ans += int(num)
    #     # print(line.find([0-9]))
print('ans = ')
print(ans)
# print(getDigitFromWord("three"))
print('***********end**********end*******')
