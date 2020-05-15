# Code for the Beginner Battleship Challenge
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
def simple_battleship():
    global letters #Lets you use the letters list inside this function
    # Write your code below:

def transposed_battleship(transposed):
    global letters #Lets you use the letters list inside this function
    # Write your code below:

def blockade(blockIdx):
    global letters #Lets you use the letters list inside this function
    # Write your code below:
    
# Now compare your output from below to what's shown in the README document.

print("\n### Part 1: Simple Battleship ###\n")
simple_battleship()
print("\n### Part 2: Transposed Battleship ###\n")
transposed_battleship(False)
print("\n")
transposed_battleship(True)
print("\n### Part 3: Blockade ###\n")
blockades = [1, 4, 9, 'a', 'd', 'i']
for idx in blockades:
    blockade(idx)
    print("\n")
