# Code for the Beginner Battleship Challenge
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
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

print("*** Part 1: Simple Battleship ***")
simple_battleship()
print("*** Part 2: Transposed Battleship ***")
transposed_battleship(False)
print("\n")
transposed_battleship(True)
print("*** Part 3: Blockade ***")
blockades = [1, 6, 12, 'a', 'j', 'l']
for idx in blockades:
    blockade(idx)
    print("\n")
