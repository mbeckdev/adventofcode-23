print('**********************')
print('***start***')
# Open the file in read mode ('r')
with open('p1input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Print each line
for line in lines:
    print(line.strip())

print('***********end**************')