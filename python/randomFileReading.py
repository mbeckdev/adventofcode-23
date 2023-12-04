# import os
# # print("Current working directory:", os.getcwd())
# puzzleNo = "1"

# testPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "test.txt"]
# testPath = "".join(testPathStringsList)
# # print('testPath = ',testPath)
# realPathStringsList = ["python\\puzzle", puzzleNo, "\\p", puzzleNo, "input.txt"]
# realPath = "".join(realPathStringsList)
# # print('realPath = ',realPath)

# # all these work:   - the r before the string does the same as  \\   \\ in a normal string
# # myfilepath = r"python\puzzle1\p1test.txt"
# # myfilepath = os.path.abspath(r"python\puzzle1\p1test.txt")
# # myfilepath = os.path.abspath(r"python/puzzle1/p1test.txt")


# myfile = open(testPath, "r")
# # myfile = open(realPath, "r")
# # myfile = open(myfilepath, "r")
# # myfile = open("python\puzzle1\p1input.txt", "r")
# # check with 
# print(myfile.read())

# print('********** start ********** start *******')
# # Open the file in read mode ('r')
# # with open(myfile, 'r') as file:
# # with open('p1input.txt', 'r') as file:
# # with myfile as file:
# with open(testPath, "r") as file:
#     # Read all lines into a list
#     # print(myfile.read())
#     lines = file.readlines()
#     print(lines)
#     # # Print each line
#     for line in lines:
#         # print(line)   # line is like 1abc2df
#         print(line.strip())    # the strip gets rid of spaces and crlf 's  line is ilke 3sfd1fj
#     #     # print(line[0])
#     #     for char in line:
#     #         print(char)
#     #     # print(line.find([0-9]))
# print('***********end**********end*******')


# # print(myfile.read())
# # myfile = open("blah.txt", "r")
# # myfile = open("C:\Users\Miche\dev\workspace\adventofcode-23\python\puzzle1\p1input.txt", "r")

# # # Specify the path to your .txt file
# # file_path = 'p1input.txt'

# # # Open the file in read mode ('r')
# # with open(file_path, 'r') as file:
# #     # Read the entire contents of the file into a string
# #     file_content = file.read()

# #     # Alternatively, you can read the file line by line
# #     # for line in file:
# #     #     print(line.strip())

# # # Now you can use the file content as needed
# # print(file_content)
