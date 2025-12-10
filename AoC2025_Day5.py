#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2025: Day 5
Created on Tue Dec  9 15:51:48 2025
@author: mrutala

--- Day 5: Cafeteria ---

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

    Ingredient ID 1 is spoiled because it does not fall into any range.
    Ingredient ID 5 is fresh because it falls into range 3-5.
    Ingredient ID 8 is spoiled.
    Ingredient ID 11 is fresh because it falls into range 10-14.
    Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?


"""

part_one = False
part_two = True

# # Test inputs
# inputs = ['3-5',
#           '10-14',
#           '16-20',
#           '12-18',
#           '9-21', # ADDED FOR TESTING
#           '',
#           '1',
#           '5',
#           '8',
#           '11',
#           '17',
#           '32',]

# Real inputs
with open('/Users/mrutala/projects/Advent-of-Code-2025/inputs/AoC2025_Day5_input.txt', 'r') as file:
    inputs = [line.rstrip() for line in file]

# Parse the two elements of the list
gap_line = inputs.index('')
fresh_ranges = inputs[0:gap_line]
ingredient_IDs = inputs[gap_line+1:]

fresh_ingredient_total = 0
for iID in ingredient_IDs:
    for r in fresh_ranges:
        lower, upper = r.split('-')
        if (int(iID) >= int(lower)) & (int(iID) <= int(upper)):
            fresh_ingredient_total += 1
            break
   
import tqdm         

# Generate a list of all fresh ingredients from fresh_ranges
# Ignore overlap (i.e., it's allowed)
all_possible_fresh_ingredients = 0
previous_ranges = []
for r in tqdm.tqdm(fresh_ranges):
    mod=0
    
    # Getting starting and stopping values
    lower, upper = [int(elem) for elem in r.split('-')]
    
    # Check if either bound falls in any already-checked range
    for previous_range in previous_ranges:
        
        if (lower >= previous_range[0]) & (lower <= previous_range[1]):
            # If the lower bound is in a previous range, 
            # increase the lower bound to the top of this range
            lower = previous_range[1] + 1

        if (upper >= previous_range[0]) & (upper <= previous_range[1]):
            # If the upper bound is in a previous range,
            # decrease the upper bound to the bottom of this range
            upper = previous_range[0] - 1
            
        if (lower < previous_range[0]) & (upper > previous_range[1]):
            # If a previous range fits *entriely* in this range,
            # Subtract off the extent of the previous range without changing 
            # Upper and lower
            mod += previous_range[1] - previous_range[0] + 1
    
    # If one range is entirely inside a previous one, lower > upper
    # Skip these
    if upper >= lower:
            
        # Count how many IDs fall in range
        number_in_range = upper - lower + 1 - mod
        
        # Record everything
        all_possible_fresh_ingredients += number_in_range
        previous_ranges.append([lower, upper])

    

# fresh_ingredient_total = 0
# for iID in ingredient_IDs:
#     if iID in all_fresh_ingredients:
#         fresh_ingredient_total +=1
        
print("Total fresh ingredients: {}".format(fresh_ingredient_total))
print("Total possible fresh ingredients: {}".format(all_possible_fresh_ingredients))