import os
puzzleNo = "1"
partNo = "1"

testPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "test", partNo, ".txt"]
testPath = "".join(testPathStringsList)
realPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "input", partNo, ".txt"]
realPath = "".join(realPathStringsList)
# print(realPath)

print('********** start ********** start *******')
# with open(testPath, "r") as file:
with open(realPath, "r") as file:
    lines = file.readlines()
    # print(lines)
    ans = 0
    for line in lines:
        # print(line)   # line is like 1abc2df
        # print(line.strip())    # the strip gets rid of spaces and crlf 's  line is ilke 3sfd1fj
        first = "empty"
        last = "empty"
        for char in line:
            if char.isdigit() and first == "empty":
                first = char
                # print(char)
            if char.isdigit():
                last = char
                # print(char)
        num = int(first + last)
        # print("num = ")
        # print(num)
        ans += num
    #     # print(line.find([0-9]))
print('***********end**********end*******')
print(ans)
