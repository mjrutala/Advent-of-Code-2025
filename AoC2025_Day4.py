#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025: Day 3
Created on Tue Dec  9 12:01:15 2025
@author: mrutala

--- Day 4: Printing Department ---

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?


"""

part_one = False
part_two = True

# # Test inputs
# inputs = ['..@@.@@@@.',
#           '@@@.@.@.@@',
#           '@@@@@.@.@@',
#           '@.@@@@..@.',
#           '@@.@@@@.@@',
#           '.@@@@@@@.@',
#           '.@.@.@.@@@',
#           '@.@@@.@@@@',
#           '.@@@@@@@@.',
#           '@.@.@@@.@.']

# Real inputs
with open('/Users/mrutala/projects/Advent-of-Code-2025/inputs/AoC2025_Day4_input.txt', 'r') as file:
    inputs = [line.rstrip() for line in file]

# Pad the input with empties all around
buffered_inputs = ['.'+row+'.' for row in inputs]
buffered_inputs.insert(0, '.'*len(buffered_inputs[0]))
buffered_inputs.append('.'*len(buffered_inputs[0]))

accessible_rolls = 0

changing_inputs = buffered_inputs
while True:
    starting_accessible_rolls = accessible_rolls
    coords_to_be_removed = []
    for row_index, row in enumerate(changing_inputs):
        for col_index, elem in enumerate(row):
            
            if elem == '@':
                # Check the neighbors
                above = changing_inputs[row_index-1][col_index-1:col_index+2]
                below = changing_inputs[row_index+1][col_index-1:col_index+2]
                sides = row[col_index-1] + row[col_index+1]
                
                all_neighbors = above + sides + below
                
                neighboring_rolls = all_neighbors.count('@')
                
                if neighboring_rolls < 4:
                    accessible_rolls +=1
                    coords_to_be_removed.append([row_index, col_index])
    
    # Remove the rolls, changing the input
    if ((accessible_rolls > starting_accessible_rolls)) & (part_two == True):
        for index in coords_to_be_removed:
            row = changing_inputs[index[0]]
            changing_inputs[index[0]] = row[:index[1]] + '.' + row[index[1]+1:]
    else:
        break
    
    print(accessible_rolls)
                
print("Number of Accessible Rolls: {}".format(accessible_rolls))
            
            