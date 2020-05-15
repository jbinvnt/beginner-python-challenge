# Beginner K-12 Python Coding Challenge
Scenario: A board game company needs your help printing out boards for their battleship games. They have three tasks for you. The starter code is in the [battleship.py](battleship.py) file.

## Part 1: Simple Battleship
*Write your code for this part inside the function defined as `def simple_battleship():`.*

The simple battleship board has a 12 by 12 grid with each square marked by a number and letter pair. Its structure is shown below (the `...` indicates a continuation, so don't have your code actually print the dots!):
```
a1 a2 a3 ...
b1 b2
c1   .
.     .
.      .
.
```
Use two `for` loops to print out the entire simple battleship board. *Hint: You will need to give each of your two for loops a list to iterate over. One of these lists is given to you already in the starter code, and you will need to create the other list yourself using the `range()` function.*

## Part 2: Transposed Battleship
*Write your code for this part inside the function defined as `def transposed_battleship(transposed):`.*

Now the company needs you to create a function that can print out some of the boards with a unique letter for every row and other boards with a unique letter for every column. If the variable `transposed` is equal to `False` then the output should be the same as Part 1. Otherwise, the output should look like this:
```
a1 b1 c1 ...
a2 b2
a3   .
.     .
.      .
.
```
You are only allowed to use two `for` loops in this function! *Hint: You can create additional variables to give the two loops different lists depending on the value of `transposed`.*

## Part 3: Blockade
*Write your code for this part inside the function defined as `def blockade(blockIdx):`.*

Finally, the company wants to add a feature where either an entire row or an entire column can be blocked off. A blocked space will have a `**` printed in its place. The board will have the same structure as it did in Part 1, except for the blocked row or column--which will be filled with `**`. The `blockIdx` variable will tell you which row or column should be blocked. For example. when `blockIdx` equals `b`, the board will look like this:

```
a1 a2 a3 ...
** ** ** ...
c1 c2 c3 ...
.       .
.         .
.           .
```
